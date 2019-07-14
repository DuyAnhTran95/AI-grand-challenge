## happy path
* greet
    - utter_greet
* request_document
    - document_form
    - form{"name": "document_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## unhappy path
* greet
    - utter_greet
* request_document
    - document_form
    - form{"name": "document_form"}
* chitchat
    - utter_chitchat
    - document_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## very unhappy path
* greet
    - utter_greet
* request_document
    - document_form
    - form{"name": "document_form"}
* chitchat
    - utter_chitchat
    - document_form
* chitchat
    - utter_chitchat
    - document_form
* chitchat
    - utter_chitchat
    - document_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop but continue path
* greet
    - utter_greet
* request_document
    - document_form
    - form{"name": "document_form"}
* stop
    - utter_ask_continue
* affirm
    - document_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop and really stop path
* greet
    - utter_greet
* request_document
    - document_form
    - form{"name": "document_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## chitchat stop but continue path
* request_document
    - document_form
    - form{"name": "document_form"}
* chitchat
    - utter_chitchat
    - document_form
* stop
    - utter_ask_continue
* affirm
    - document_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## stop but continue and chitchat path
* greet
    - utter_greet
* request_document
    - document_form
    - form{"name": "document_form"}
* stop
    - utter_ask_continue
* affirm
    - document_form
* chitchat
    - utter_chitchat
    - document_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat stop but continue and chitchat path
* greet
    - utter_greet
* request_document
    - document_form
    - form{"name": "document_form"}
* chitchat
    - utter_chitchat
    - document_form
* stop
    - utter_ask_continue
* affirm
    - document_form
* chitchat
    - utter_chitchat
    - document_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## chitchat, stop and really stop path
* greet
    - utter_greet
* request_document
    - document_form
    - form{"name": "document_form"}
* chitchat
    - utter_chitchat
    - document_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## Generated Story 3490283781720101690 (example from interactive learning, "form: " will be excluded from training)
* greet
    - utter_greet
* request_document
    - document_form
    - form{"name": "document_form"}
    - slot{"requested_slot": "level"}
* chitchat
    - utter_chitchat  <!-- document was predicted by FormPolicy and rejected, other policy predicted utter_chitchat -->
    - document_form
    - slot{"requested_slot": "type_exam"}
* form: inform{"type_exam": "beginner"}
    - slot{"type_exam": "toeic"}
    - form: document_form
    - slot{"type_exam": "toeic"}
    - slot{"requested_slot": "level"}
* form: inform{"level": "beginner"}
    - form: document_form
    - slot{"level": "beginner"}
* chitchat
    - utter_chitchat
* stop
    - utter_ask_continue
* affirm
    - document_form 
* form: affirm
    - form: document_form
    - utter_slots_values
* thankyou
    - utter_noworries

## New Story

* request_document
    - document_form
    - slot{"requested_slot":"level"}
* inform{"level":"beginner"}
    - document_form
    - slot{"level":"beginner"}
    - slot{"requested_slot":"type_exam"}
* inform{"type_exam":"toeic"}
    - document_form
    - slot{"type_exam":"toeic"}
    - slot{"requested_slot":null}
    - utter_slots_values

## New Story

* request_document{"type_exam":"toeic"}
    - document_form
    - slot{"requested_slot":"level"}
* inform
    - action_default_fallback
* inform
    - action_default_fallback
