from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.types import DomainDict

from dummy_data.data import weather_data, weather_summary
from actions.helpers import parse_date


class ActionWeatherSearch(Action):
    
    def name(self) -> Text:
        return "action_weather_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = tracker.get_slot("location")
        date  = tracker.get_slot("date")
        date = parse_date(date)
        condition  = tracker.get_slot("weather_condition")

        if not condition:
            condition = "කාලගුණය"
        return [SlotSet("weather", weather_data[location][date][condition])]


class ActionWeatherSummarySearch(Action):
    
    def name(self) -> Text:
        return "action_weather_summary_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        date  = tracker.get_slot("date")
        parsed_date = parse_date(date)

        if parse_date:
            if -4 < parsed_date < 4:
                dispatcher.utter_message(text="{} දින කාලගුණ සාරාංශය සොයමින් පවතී.".format(date))
                return [SlotSet("summary", weather_summary[parsed_date])]
            else:
                dispatcher.utter_message(text="date {} not in range".format(date))
                return []
        else:
            dispatcher.utter_message(text="invalid date {}".format(date))
            return []


class ActionResetWeatherCondition(Action):
    
    def name(self) -> Text:
        return  "action_reset_weather_condition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return[SlotSet("weather_condition", None)]


class ValidateWeatherForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_weather_form"

    def validate_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:

        parsed_date = parse_date(slot_value)
        print("hi")
        if parsed_date:
            if -4 < parsed_date < 4:
                return {"date": slot_value}
            else:
                dispatcher.utter_message(text="date {} not in range".format(slot_value))
                return {"date": None}
        else:
            dispatcher.utter_message(text="invalid date {}".format(slot_value))
            return {"date": None}

