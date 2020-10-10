# from abc import ABC
from .helpers import check_type

class Payloads:
    PLATFORM_BOTNOI_SME = "botnoi-sme"
    SUPPORTED_PLATFORMS = [PLATFORM_BOTNOI_SME]
    SUPPORTED_CHATBOTS = ["line"]
    def __init__(self, chatbots:list=["line"], platform:str=PLATFORM_BOTNOI_SME):
        '''
        :param chatbots: list of available chatbots to create payloads
        :param platform: specify platform to use (now support only botnoi-sme)
        '''
        # Verify parameter types
        check_type(chatbots, list, can_be_none=False)
        check_type(platform, str, can_be_none=False)

        # Verify supported chatbot platform
        if not all(chatbot in chatbots for chatbot in self.SUPPORTED_CHATBOTS):
            raise Exception("chatbots are not supported")
        if (platform not in self.SUPPORTED_PLATFORMS):
            raise Exception("Platform {platform} is not supported")

        # keep internal variables
        self.__platform = platform
        self.__chatbots = chatbots
        self.__data = {}

    def __iter__(self):
        # should translate into specific platform's payloads
        keys = self.__data.keys()
        for key in keys:
            yield key, self.__data[key]
        # return dict(self.__data)