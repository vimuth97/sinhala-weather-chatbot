# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from dummy_data.data import weather_data
from actions.helpers import parse_date

class ActionWeatherSearch(Action):

    def name(self) -> Text:
        return "action_weather_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = tracker.get_slot("location")
        date  = tracker.get_slot("date")
        parsed_date = parse_date(date)
        if parse_date:
            if -8 < parsed_date < 8:
                dispatcher.utter_message(text="{} දින {} කාලගුණ තොරතුරු සොයමින් පවතී.".format(date, location))
                return [SlotSet("weather", weather_data[location][parsed_date]["කාලගුණය"])]
            else:
                dispatcher.utter_message(text="date {} not in range".format(date))
                return []
        else:
            dispatcher.utter_message(text="invalid date {}".format(date))
            return []

class ActionWeatherConditionSearch(Action):
    
    def name(self) -> Text:
        return "action_weather_condition_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = tracker.get_slot("location")
        date  = tracker.get_slot("date")
        condition  = tracker.get_slot("weather_condition")
        parsed_date = parse_date(date)

        dispatcher.utter_message(text="{} දින {} කාලගුණ තොරතුරු සොයමින් පවතී.".format(date, location))
        if parse_date:
            if -8 < parsed_date < 8:
                dispatcher.utter_message(text="{} දින {} කාලගුණ තොරතුරු සොයමින් පවතී.".format(date, location))
                return [SlotSet("weather_condition_results", weather_data[location][date][condition])]
            else:
                dispatcher.utter_message(text="date {} not in range".format(date))
                return []
        else:
            dispatcher.utter_message(text="invalid date {}".format(date))
            return []

