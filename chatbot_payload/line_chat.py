from .helpers import check_type as __type_check


def line_text_message(message: str):
    __type_check(message, str, can_be_none=False)
    return {
        "type": "text",
        "text": message[:5000]
    }


def line_sticker_message(package_id: str, sticker_id: str):
    __type_check(package_id, str, can_be_none=False)
    __type_check(sticker_id, str, can_be_none=False)
    return {
        "type": "sticker",
        "packageId": package_id,
        "stickerId": sticker_id
    }
