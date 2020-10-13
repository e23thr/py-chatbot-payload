# from abc import ABC
import inspect
from .helpers import check_type
from .facebook_chat import *
from .line_chat import *


def parse_line(rows: list):
    result = []
    for row in rows:
        if row["type"] == "text":
            result.append(line_text_message(row["data"]))

        if row["type"] == "sticker":
            result.append(line_sticker_message(row["data"]["packageId"], row["data"]["stickerId"]))
    return result


def parse_facebook(rows: list):
    result = []
    for row in rows:
        if row["type"] == "text":
            result.append(facebook_text_message(row["data"]))
    return result


class Payloads:
    PLATFORM_BOTNOI_SME = "botnoi-sme"
    SUPPORTED_PLATFORMS = [PLATFORM_BOTNOI_SME]
    CHAT_BOT_LINE = "line"
    CHAT_BOT_FACEBOOK = "facebook"
    SUPPORTED_CHAT_BOTS = [CHAT_BOT_LINE]

    def __init__(self, chat_bots: list = ["line"], platform: str = PLATFORM_BOTNOI_SME):
        """
        :param chatbots: list of available chatbots to create payloads
        :param platform: specify platform to use (now support only botnoi-sme)
        """
        # Verify parameter types
        check_type(chat_bots, list, can_be_none=False)
        check_type(platform, str, can_be_none=False)

        # Verify supported chatbot platform
        if not all(chat_bot in chat_bots for chat_bot in self.SUPPORTED_CHAT_BOTS):
            raise Exception("chatbots are not supported")
        if platform not in self.SUPPORTED_PLATFORMS:
            raise Exception("Platform {platform} is not supported")

        # keep internal variables
        self.__platform = platform
        self.__chat_bots = chat_bots
        self.__data = {k: [] for k in self.__chat_bots}

    def __iter__(self):
        # should translate into specific platform's payloads
        keys = self.__data.keys()
        data = {}
        for key in keys:
            # self.CHAT_BOT_LINE
            # print("Key: ", key)
            # print("Data", self.__data[key])
            if key == self.CHAT_BOT_LINE:
                data[key] = parse_line(self.__data[key])

            # self.CHAT_BOT_FACEBOOK
            if key == self.CHAT_BOT_FACEBOOK:
                data[key] = parse_facebook(self.__data[key])

            yield key, data[key]

    def __check_if_chatbot_is_available(self, chat_bot, possible_chat_bots=[]):
        is_supported_chatbot = chat_bot in self.__chat_bots and chat_bot in possible_chat_bots
        if not is_supported_chatbot:
            raise Exception(f"Chatbot {chat_bot} not supported by function {inspect.stack()[1][3]}")

    # public functions
    def text_message(self, message: str, chat_bot: str = CHAT_BOT_LINE):
        """
        Create a text message payload

        :param message: (str) Text message to reply
        :param chat_bot: (str) one of instance.CHAT_BOT_LINE, instance.CHAT_BOT_FACEBOOK
        :return: None
        """
        self.__check_if_chatbot_is_available(chat_bot=chat_bot,
                                             possible_chat_bots=[self.CHAT_BOT_LINE, self.CHAT_BOT_FACEBOOK])
        self.__data[chat_bot].append({
            "type": "text",
            "data": message
        })
        print("DEBUG", self.__data)

    def sticker_message(self, package_id: str, sticker_id: str, chat_bot: str = CHAT_BOT_LINE):
        """
        Create a sticker message payload (now available only line chatbot)
        :param package_id: (str) Sticker package id
        :param sticker_id: (str) Sticker id
        :param chat_bot: (str) only instance.CHAT_BOT_LINE
        :return: None
        """
        self.__check_if_chatbot_is_available(chat_bot=chat_bot,
                                             possible_chat_bots=[self.CHAT_BOT_LINE])

        self.__data[chat_bot].append({
            "type": "sticker",
            "data": {
                "packageId": package_id,
                "stickerId": sticker_id
            }
        })

    def image_message(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        chat_bot = kwargs["chatbot"]
        self.__check_if_chatbot_is_available(chat_bot=chat_bot,
                                             possible_chat_bots=[self.CHAT_BOT_LINE, self.CHAT_BOT_FACEBOOK])

        data = {"type": "image", "data": {}}
        if chat_bot in [self.CHAT_BOT_LINE]:
            original_url = kwargs["original_url"]
            preview_url = kwargs["preview_url"]
            check_type(original_url, str, can_be_none=False)
            check_type(preview_url, str, can_be_none=False)
            data['data'] = {
                "originalContentUrl": original_url,
                "previewImageUrl": preview_url
            }

        if chat_bot in [self.CHAT_BOT_FACEBOOK]:

            pass

        self.__data[chat_bot].append(data)
