import os
from dotenv import load_dotenv
load_dotenv()
from typing import Literal, Optional, Any
from utils.config_loader import load_config
from langchain_groq import ChatGroq 
from pydantic import BaseModel, Field

class ConfigLoader:
    def __init__(self):
        print("Loaded config")
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]

class ModelLoader(BaseModel):
    model_provider : Literal["groq"] = "groq"
    config : Optional[ConfigLoader] = Field(default = None, exclude = True)
    def __init__(self):
        pass 
    
    def model_post_init(self, __context : Any) -> None:
        self.config = ConfigLoader

    class Config:
        arbitrary_types_allowed = True
    
    def load_llm(self):
        """
        Load and return the LLM model
        """
        print("Setting up the LLM model..")
        print("Loading the model from the provider : ",{self.model_provider})
        if self.model_provider == "groq":
            print("Loading LLM from groq...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model_name = model_name, groq_api_key = groq_api_key)
        
        return llm