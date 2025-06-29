from utils.model_loader import ModelLoader
from prompt_library import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessageState, END, START
from langgraph.prebuilt import ToolNode, tools_condition


class GraphBuilder:
    def __init__(self, graph):
        self.tools = [

        ] 


        self.system_prompt = SYSTEM_PROMPT

    def agent_function(self):
        """
        Main agent function
        """
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = llm_with_tools.invoke(input_question)
        return {"Messages" : {response}}

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
        