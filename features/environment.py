from behave import *
from chatbot_payload import ChatbotPayloads

cbp: ChatbotPayloads = None


def before_step(context, step):
    if step.keyword == "Given":
        chatbots = context.active_outline["chatbots"].split(",")
        platform = context.active_outline["platform"]
        context.my_object:ChatbotPayloads = ChatbotPayloads(chat_bots=chatbots,
                                      platform=platform)
