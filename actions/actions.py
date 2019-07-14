# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

import json


data = {
    "beginner":{
        "toeic":{
            "url":"http://www.flyhigh.edu.vn/tailieu/11/tai-lieu-luyen-thi-toeic-cho-nguoi-moi-bat-dau",
            "description":"Cố gắng bạn nhé !! Cái gì khởi đầu cũng khó khăn mà !Mình ngày xưa cũng học tệ lắm"
        },
        "ielts":{
            "url":"http://ielts-fighter.com/supportskill/Bo-tai-lieu-luyen-thi-IELTS-nao-phu-hop-cho-nguoi-moi-bat-dau-Level-4-0-4-5_mt1463654000.html",
            "description":"IELTS khá khó nhưng đứng nản các bạn nhé !!"
        },
        "toefl":{
            "url":"https://edu2review.com/reviews/lo-trinh-hoc-toefl-cho-nguoi-moi-bat-dau-5124.html",
            "description":"Bạn xem link này nhé, hì hì, Toefl là hơi khó nhai đó nhen"
        }
    },

    "intermediate":{
        "toeic":{
            "url":"https://nghetienganhpro.com/tai-lieu-on-thi-toeic-longman-preparation-series-intermediate-course/",
            "description":"Chắc chắn bộ tài liệu Long Man này dành cho bạn, triển thôi :))"
        },
        "ielts":{
            "url":"https://ielts-share.com/tai-lieu-tu-hoc-ielts-ca-4-ki-nang-cho-moi-trinh-band-4-0-7-0",
            "description":"Bộ tài liệu này phù hợp cho nhiều band, bạn có thể lựa chọn phù hợp cho bản thân nhé :))"
        },
        "toefl":{
            "url":"https://www.dolenglish.vn/ielts-library/blogs/6-cuon-sach-luyen-thi-toefl-ibt-2019",
            "description":"Đây là những quyền sách tốt nhất !! Bạn cố gắng lên nhé !!"
        }
    },

    "good":{
        "toeic":{
            "url":"https://www.anhngumshoa.com/tin-tuc/tat-tan-tat-tai-lieu-tu-hoc-toeic-cho-moi-cap-do-37147.html",
            "description":"Bạn giỏi thế thì mình nghĩ bạn nên tìm tài liệu học IELTS á !! "
        },
        "ielts":{
            "url":"http://zim.vn/tu-sach-ielts-band-8/",
            "description":"Bạn thừa sức đọ nó đúng không =))"
        },
        "toefl":{
            "url":"http://oxford.edu.vn/goc-tieng-anh/kinh-nghiem-luyen-thi-toefl/tai-lieu-luyen-thi-toefl-mien-phi-644.html",
            "description":"Mình thấy cứ tài liệu oxford mà triển thôi "
        }
    }
}

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

        type_exam = tracker.get_slot('type_exam')
        level = tracker.get_slot('level')
    
        response = data[level][type_exam]
        print('check response', response)
        # utter submit template
        dispatcher.utter_message("Đây là link tài liệu tài liệu {}. {}".format(response['url'], response['description']))
        return []




data_location = [
    {
        "calendar": [
            {
                "date": " 06 tháng 7 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": " 24 tháng 8 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "  07 tháng 9 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": " 12 tháng 9 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": " 16 tháng 11 2019",
                "type": [
                    "Học thuật "
                ]
            },
            {
                "date": " 14 tháng 12 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát\n"
                ]
            }
        ],
        "title": "Hà Nội",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "22 tháng 6 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "20 tháng 7 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "10 tháng 8 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "14 tháng 9 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "12 tháng 10 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "16 tháng 11 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "14 tháng 12 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "TP. Hồ Chí Minh",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "13 tháng 6 2019",
                "type": [
                    "Học thuật "
                ]
            },
            {
                "date": "29 tháng 6 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát  "
                ]
            },
            {
                "date": "18 tháng 7 2019",
                "type": [
                    "Học thuật  "
                ]
            },
            {
                "date": "27 tháng 7 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát  "
                ]
            },
            {
                "date": "10 tháng 8 2019",
                "type": [
                    "Học thuật "
                ]
            },
            {
                "date": "24 tháng 8 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "12 tháng 9 2019",
                "type": [
                    "Học thuật "
                ]
            },
            {
                "date": "28 tháng 9 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát  "
                ]
            },
            {
                "date": "12 tháng 10 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát  "
                ]
            },
            {
                "date": "26 tháng 10 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát  "
                ]
            },
            {
                "date": "07 tháng 11 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát  "
                ]
            },
            {
                "date": "23 tháng 11 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát  "
                ]
            },
            {
                "date": "07 tháng 12 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát  "
                ]
            },
            {
                "date": "14 tháng 12 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát  "
                ]
            }
        ],
        "title": "Hải Phòng",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "27 tháng 7 2019",
                "type": [
                    "Học thuật"
                ]
            }
        ],
        "title": "Hạ Long",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "06 tháng 7 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "28 tháng 9 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "23 tháng 11 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "Bắc Giang",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [],
        "title": "Phú Thọ",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "12 tháng 10 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "Thanh Hóa",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "17 tháng 8 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "28 tháng 9 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "Vinh",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "01 tháng 6 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "22 tháng 6 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "06 tháng 7 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "27 Tháng 7 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "10 tháng 8 2019",
                "type": [
                    "Học thuật "
                ]
            },
            {
                "date": "24 tháng 8 2019",
                "type": [
                    "Học thuật "
                ]
            },
            {
                "date": "07 tháng 9 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "28 tháng 9 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "12 tháng 10 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "26 tháng 10 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "16 tháng 11 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "30 tháng 11 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "14 Tháng 12 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "Huế",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "22 tháng 6 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "27 tháng 7 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "17 tháng 8 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "14 tháng 9 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "26 tháng 10 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "16 tháng 11 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "14 tháng 12 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "Đà Nẵng",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "29 tháng 6 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "17 tháng 8 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "19 tháng 10 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "07 tháng 12 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "Quy Nhơn",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "27 Tháng 7 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "07 tháng 9 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "23 tháng 11 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "Phú Yên",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [],
        "title": "Quảng Ngãi",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "02 Tháng 11 2019",
                "type": [
                    "Học thuật"
                ]
            }
        ],
        "title": "Buôn Ma Thuột",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "12 tháng 1 2019",
                "type": [
                    "Học thuật"
                ]
            }
        ],
        "title": "Kon Tum",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "20 tháng 7 2019",
                "type": [
                    "Học thuật "
                ]
            },
            {
                "date": "16 tháng 11 2019",
                "type": [
                    "Học thuật "
                ]
            }
        ],
        "title": "Gia Lai",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "01 tháng 6 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "27 tháng 7 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "28 tháng 9 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "23 tháng 11 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "Nha Trang",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "17 tháng 8 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "23 tháng 11 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "Đà Lạt",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "29 tháng 6 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "20 tháng 7 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "17 tháng 8 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "28 tháng 9 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "26 tháng 10 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "23 tháng 11 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "14 tháng 12 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "Vũng Tàu",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "1 tháng 6 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "22 tháng 6 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "6 tháng 7 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát "
                ]
            },
            {
                "date": "27 tháng 7 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "17 tháng 8 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "28 tháng 9 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "26 tháng 10 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "23 tháng 11 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát "
                ]
            },
            {
                "date": "7 tháng 12 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "14 tháng 12 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "Biên Hòa",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "17 tháng 8 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "28 tháng 9 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "26 tháng 10 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "23 tháng 11 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "14 tháng 12 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "Đồng Tháp",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "29 tháng 6 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "17 tháng 8 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "26 tháng 10 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "14 tháng 12 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "Cần Thơ",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "22 tháng 6 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "07 tháng 9 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "07 tháng 12 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "Ngày thi và đia điểm thi với đối tác củaBình Dương",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "27 tháng 7 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            },
            {
                "date": "16 tháng 11 2019",
                "type": [
                    "Học thuật"
                ]
            }
        ],
        "title": "Trà Vinh",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "22 tháng 6 2019",
                "type": [
                    "Học thuật"
                ]
            },
            {
                "date": "02 tháng 11 2019",
                "type": [
                    "Học thuật"
                ]
            }
        ],
        "title": "Vĩnh Long",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    },
    {
        "calendar": [
            {
                "date": "09 tháng 2 2019",
                "type": [
                    "Học thuật ",
                    " Tổng quát"
                ]
            }
        ],
        "title": "An Giang",
        "contact": {
            "website": "www.agfivestar.vn",
            "phone": "Hotline: +84 (0)936 398192"
        },
        "place": [
            "Học viện Anh ngữ 5 sao Atlantic Five-Star English",
            " 125 Hoàng Ngân, Trung Hoà, Cầu Giấy ",
            "33 Lạc Trung, Hai Bà Trưng, Hà Nội"
        ],
        "fee": {
            "academic": 4750000,
            "general": 4750000
        }
    }
]



class LocationForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "location_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["location", "type_exam"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "location": 
            self.from_entity(entity="location", not_intent="chitchat"),
            "type_exam": 
            self.from_entity(
                    entity="type_exam", intent=["inform", "request_document"])
        }

    # USED FOR DOCS: do not rename without updating in docs
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
    def validate_location(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[Text]:
        """Validate cuisine value."""

        return {"location":value}

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

        type_exam = tracker.get_slot('type_exam')
        location_entity = tracker.get_slot('location')

        print('check ', type_exam, location_entity)
        response = {}
        if type_exam=='ielts':
            for location in data_location:
                if(location['title'].lower().replace(" ", "") in location_entity):
                    
                    response['date'] = location['calendar'][len(location['calendar'])-1]['date']
                    response['location'] = ','.join(location['place'])
                    response['contact'] = ','.join(location['contact'])


            print('check response', response)
            # utter submit template
            dispatcher.utter_message("Hôi đồng Anh tổ chức IELTS tại {}, vào ngày {}. Bạn có thể liên hệ {}. Nhớ đăng ký sớm nhé :)) "
            .format(response['location'], response['date'], response['contact']))
        else:
            dispatcher.utter_message("Mình chưa có thông tin gì về cuộc thi này :(( Sorry bạn nhé !")
        return []

