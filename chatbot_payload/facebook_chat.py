from .helpers import check_type as __type_check


def facebook_text_message(message: str):
    __type_check(message, str, can_be_none=False)
    return {
        "text": message
    }