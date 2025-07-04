import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper 

class GooglePlaceSearchTool:
    def __init__(self, api_key: str):
        self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
        self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)
    
    def google_search_attractions(self, place: str) -> dict:
        """
        Searches for top tourist attractions in and around the specified location using the Google Places API.

        Args:
            place (str): The name of the place to search.

        Returns:
            dict: Search results containing notable tourist attractions.
        """
        return self.places_tool.run(f"top attractive places in and around {place}")


    def google_search_restaurants(self, place: str) -> dict:
        """
        Searches for highly rated restaurants and eateries in and around the specified location using the Google Places API.

        Args:
            place (str): The location for which restaurants should be listed.

        Returns:
            dict: Search results containing top restaurants and dining options.
        """
        return self.places_tool.run(f"what are the top 10 restaurants and eateries in and around {place}?")


    def google_search_activity(self, place: str) -> dict:
        """
        Searches for popular tourist activities and experiences available in and around the specified place using the Google Places API.

        Args:
            place (str): The destination to search for activities.

        Returns:
            dict: Search results listing popular tourist activities.
        """
        return self.places_tool.run(f"Activities in and around {place}")


    def google_search_transportation(self, place: str) -> dict:
        """
        Searches for transportation options such as public transit, taxis, and rentals available in the specified location using the Google Places API.

        Args:
            place (str): The name of the location to search transportation options for.

        Returns:
            dict: Search results listing transportation modes in the area.
        """
        return self.places_tool.run(f"What are the different modes of transportations available in {place}")

    def google_search_hotels(self, place: str) -> str:
        """
        Searches for well-rated hotels in the specified location.

        Args:
            place (str): The name of the place or city.

        Returns:
            str: A list of top hotels to stay, possibly categorized into luxury and budget options.
        """
        return self._query(f"List some highly-rated luxury and budget hotels in {place} for travelers.")

    def google_search_shopping_places(self, place: str) -> str:
        """
        Searches for popular shopping locations like markets and malls in the specified place.

        Args:
            place (str): The name of the destination.

        Returns:
            str: Descriptions of popular shopping areas, local markets, or malls.
        """
        return self._query(f"What are the best shopping streets, markets, and malls in {place}?")

    def google_search_cultural_experiences(self, place: str) -> str:
        """
        Retrieves cultural and historical places to visit at the location.

        Args:
            place (str): The city or tourist location.

        Returns:
            str: A list of cultural places such as temples, museums, forts, etc.
        """
        return self._query(f"Suggest famous cultural and historical places to explore in {place}.")

    def google_search_seasonal_highlights(self, place: str, month: str) -> str:
        """
        Fetches activity and travel suggestions based on the time of year.

        Args:
            place (str): The travel destination.
            month (str): The month of intended travel (e.g., 'August').

        Returns:
            str: A list of places or experiences that are best enjoyed in that month.
        """
        return self._query(f"What are the best places and experiences in {place} during the month of {month}?")

    def google_search_hidden_gems(self, place: str) -> str:
        """
        Finds offbeat and less-known attractions for travelers who prefer quiet or unexplored spots.

        Args:
            place (str): The destination location.

        Returns:
            str: Recommendations for hidden or underrated tourist spots.
        """
        return self._query(f"What are some hidden gems or less-crowded places to visit in and around {place}?")

    def google_search_by_travel_type(self, place: str, travel_type: str) -> str:
        """
        Recommends destinations based on the travel type (e.g., romantic, adventure, family).

        Args:
            place (str): The name of the destination.
            travel_type (str): Type of travel experience (e.g., 'romantic', 'family', 'spiritual').

        Returns:
            str: Places suitable for the specified travel type.
        """
        return self._query(f"What are the best places in {place} for a {travel_type} trip?")

    def search_local_cuisine(self, place: str) -> str:
        """
        Suggests popular local foods and the best places to try them.

        Args:
            place (str): City or area where the user is traveling.

        Returns:
            str: Famous dishes from that region and recommended eateries.
        """
        return self._query(f"What are the most famous dishes in {place} and where can travelers eat them?")


class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str) -> dict:
        """
        Searches for top tourist attractions in and around the specified location using the Google Places API.

        Args:
            place (str): The name of the place to search.

        Returns:
            dict: Search results containing notable tourist attractions.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_restaurants(self, place: str) -> dict:
        """
        Searches for highly rated restaurants and eateries in and around the specified location using the Google Places API.

        Args:
            place (str): The location for which restaurants should be listed.

        Returns:
            dict: Search results containing top restaurants and dining options.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place: str) -> dict:
        """
        Searches for popular tourist activities and experiences available in and around the specified place using the Google Places API.

        Args:
            place (str): The destination to search for activities.

        Returns:
            dict: Search results listing popular tourist activities.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for transportation options such as public transit, taxis, and rentals available in the specified location using the Google Places API.

        Args:
            place (str): The name of the location to search transportation options for.

        Returns:
            dict: Search results listing transportation modes in the area.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_hotels(self, place: str) -> dict:
        """
        Searches for well-rated hotels to stay in the specified location using TavilySearch.

        Args:
            place (str): The name of the place or city.

        Returns:
            dict: Tavily search result containing hotel recommendations.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"List some highly-rated luxury and budget hotels in {place} for travelers."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result


    def tavily_search_shopping_places(self, place: str) -> dict:
        """
        Searches for popular shopping locations like markets and malls in the specified place using TavilySearch.

        Args:
            place (str): The name of the destination.

        Returns:
            dict: Tavily search result containing popular shopping areas or markets.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the best shopping streets, markets, and malls in {place}?"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result


    def tavily_search_cultural_experiences(self, place: str) -> dict:
        """
        Retrieves cultural and historical places to visit at the location using TavilySearch.

        Args:
            place (str): The city or tourist location.

        Returns:
            dict: Tavily search result with cultural and historical landmarks.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"Suggest famous cultural and historical places to explore in {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result


    def tavily_search_seasonal_highlights(self, place: str, month: str) -> dict:
        """
        Fetches seasonal travel highlights based on the specified month using TavilySearch.

        Args:
            place (str): The travel destination.
            month (str): The month of intended travel (e.g., 'August').

        Returns:
            dict: Tavily search result with month-specific experiences or events.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the best places and experiences in {place} during the month of {month}?"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result


    def tavily_search_hidden_gems(self, place: str) -> dict:
        """
        Finds offbeat and lesser-known attractions using TavilySearch.

        Args:
            place (str): The destination location.

        Returns:
            dict: Tavily search result with hidden or unexplored tourist spots.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are some hidden gems or less-crowded places to visit in and around {place}?"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result


    def tavily_search_by_travel_type(self, place: str, travel_type: str) -> dict:
        """
        Recommends places based on the travel type using TavilySearch.

        Args:
            place (str): The name of the destination.
            travel_type (str): Type of travel experience (e.g., 'romantic', 'family', 'spiritual').

        Returns:
            dict: Tavily search result with customized suggestions for the travel type.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the best places in {place} for a {travel_type} trip?"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result


    def tavily_search_local_cuisine(self, place: str) -> dict:
        """
        Suggests popular local dishes and where to try them using TavilySearch.

        Args:
            place (str): City or area where the user is traveling.

        Returns:
            dict: Tavily search result with food recommendations and famous eateries.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the most famous dishes in {place} and where can travelers eat them?"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
