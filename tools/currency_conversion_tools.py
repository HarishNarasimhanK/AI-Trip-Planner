from utils.currency_converter import CurrencyConverter
from typing import Optional
from langchain.tools import tool
from dotenv import load_dotenv
import os



class CurrencyConverterTool:
    def __init__(self):
         load_dotenv()
         self.api_key = os.getenv("EXCHANGE_RATE_API_KEY")
         self.currency_service = CurrencyConverter(api_key=self.api_key)
         self.currency_concerter_tool_list = self._setup_tools()

    def _setup_tools(self):
         """Setup the currency conversion tools."""
         @tool
         def convert_currency(
             amount: float,
             from_currency: str,
             to_currency: str
         ) -> Optional[float]:
             """Convert the amount from one currency to another."""
             try:
                 return self.currency_service.convert(amount, from_currency, to_currency)
             except Exception as e:
                 return f"Error converting currency: {str(e)}"
          
          return [convert_currency]