from utils.model_loader import ModelLoader
from prompt_library import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessageState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from tools.weather_info_tool import WeatherInfoTool
from tools.currency_conversion_tools import CurrencyConverterTool
from tools.place_search_tool import PlaceSearchTool
from tools.calculator_tool import CalculatorTool


class GraphBuilder:
    def __init__(self, model_provider : str = "groq"):
        self.model_loader = ModelLoader(model_provider = model_provider)
        self.llm = self.model_loader.load_llm()
        self.tools = [

        ] 
        self.weather_tools = WeatherInfoTool()
        self.place_search_tools = PlaceSearchTool()
        self.currency_converter_tools = CurrencyConverterTool()
        self.calculator_tools = CalculatorTool()

        self.tools.extend([* self.weather_tools.weather_tools_list,
                           * self.place_search_tools.weather_tools_list,
                           * self.currency_converter_tools.weather_tools_list,
                           * self.calculator_tools.weather_tools_list])
        self.llm_with_tools = self.llm.bind_tools(tools = self.tools)
        self.system_prompt = SYSTEM_PROMPT

    def agent_function(self, state : MessageState):
        """
        Main agent function
        """
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"messages" : [response]}


    def build_graph(self):
        graph_builder = StateGraph(MessageState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools = self.tools))
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edges("agent", tools_condition)
        graph_builder.add_edge("tools", "agent")
        graph_builder.add_edge("agent", END)

    def __call__(self):
        return self.build_graph()
        