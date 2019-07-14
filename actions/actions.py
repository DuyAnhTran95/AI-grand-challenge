# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Hello World!")

        return []


class TimTaiLieuAction(Action):
    def name(self) -> Text:
        return "action_tim_tai_lieu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message("Hello World!")
        print('get intent tim tai lieu')
        muc_dich_slot = next(tracker.get_latest_entity_values("muc_dich"), None)
        if muc_dich_slot is None:
            dispatcher.utter_template("utter_ask_muc_dich", tracker)
        else:
            trinh_do_slot = next(tracker.get_latest_entity_values("trinh_do"), None)
            print(trinh_do_slot)
            if trinh_do_slot is None:
                dispatcher.utter_template("utter_ask_trinh_do", tracker)
            else:
                dispatcher.utter_message("https://cfl.edu.vn/tag/danh-sach-thi-toeic-quoc-te-iig/")
            return []


class TimTaiLieuForm(FormAction):

    def name(self) -> Text:
        return "tim_tai_lieu_form"

    def required_slots(tracker: Tracker) -> List[Text]:
        return ['muc_dich', 'trinh_do']

    def submit(self, dispatcher, tracker, domain) -> List[Dict]:
        return []
