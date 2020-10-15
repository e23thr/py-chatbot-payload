from .helpers import check_type as __type_check


def facebook_text_message(message: str):
    __type_check(message, str, can_be_none=False)
    return {
        "text": message
    }


def facebook_image_message(url: str, is_reusable: bool = True):
    __type_check(url, str, can_be_none=False)
    __type_check(is_reusable, bool, can_be_none=False)
    return {
        "attachment": {
            "type": "image",
            "payload": {
                "url": url,
                "is_reusable": is_reusable
            }
        }
    }


def facebook_video_message(url: str, is_reusable: bool = True):
    __type_check(url, str, can_be_none=False)
    __type_check(is_reusable, bool, can_be_none=False)
    return {
        "attachment": {
            "type": "video",
            "payload": {
                "url": url,
                "is_reusable": is_reusable
            }
        }
    }


def facebook_image_template_message(attachment_id: str = None, url: str = None):
    __type_check(attachment_id, str, can_be_none=True)
    __type_check(url, str, can_be_none=True)
    if attachment_id is None and url is None:
        raise Exception("Facebook image must have attachment_id or url")
    payload_element = {
        "media_type": "image"
    }
    if attachment_id is not None:
        payload_element["attachment_id"] = attachment_id
    if url is not None:
        payload_element["url"] = url

    payload = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "media",
                "elements": [
                    payload_element
                ]
            }
        }
    }

    return payload


def facebook_video_template_message(attachment_id: str = None, url: str = None):
    __type_check(attachment_id, str, can_be_none=True)
    __type_check(url, str, can_be_none=True)
    if attachment_id is None and url is None:
        raise Exception("Facebook image must have attachment_id or url")
    payload_element = {
        "media_type": "video"
    }
    if attachment_id is not None:
        payload_element["attachment_id"] = attachment_id
    if url is not None:
        payload_element["url"] = url

    payload = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "media",
                "elements": [
                    payload_element
                ]
            }
        }
    }

    return payload
