# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class DocumentForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "document_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["level", "type_exam"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "level": 
            self.from_entity(entity="level", not_intent="chitchat"),
            "type_exam": 
            self.from_entity(
                    entity="type_exam", intent=["inform", "request_document"])
        }

    # USED FOR DOCS: do not rename without updating in docs
    @staticmethod
    def level_db() -> List[Text]:
        """Database of supported level"""

        return [
            "beginner",
            "intermediate",
            "good"
        ]

    @staticmethod
    def type_exam_db() -> List[Text]:
        return [
            "toeic",
            "ielts",
            "toefl"
        ]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    # USED FOR DOCS: do not rename without updating in docs
    def validate_level(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """Validate cuisine value."""

        if value.lower() in self.level_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"level": value}
        else:
            dispatcher.utter_template("utter_wrong_level", tracker)
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"level": None}

    def validate_type_exam(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """Validate type_exam value."""

        if value.lower() in self.type_exam_db():
            return {"type_exam": value}
        else:
            dispatcher.utter_template("utter_wrong_type_exam", tracker)
            # validation failed, set slot to None
            return {"type_exam": None}


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        print('check okok ',tracker )
        type_exam = tracker.get_slot('type_exam')
        level = tracker.get_slot('level')
        # utter submit template
        dispatcher.utter_message("Đây là tài liệu của bạn {} và {}".format(type_exam, level))
        return []
