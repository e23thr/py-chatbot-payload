from behave import *


@given(u'Prepare chatbots')
def step_impl(context):
    pass


@when(u'a text message ("{message}") is added for "{chatbots}"')
def step_impl(context, message, chatbots):
    for chatbot in chatbots.split(","):
        context.my_object.text_message(chat_bot=chatbot, message=message)


@then(u'payload must be array having at least 1 element')
def step_impl(context):
    chatbots = context.active_outline['chatbots'].split(",")
    data = dict(context.my_object)
    for chatbot in chatbots:
        chatbot_objects = data.get(chatbot, None)
        assert type(chatbot_objects) == list
        assert len(chatbot_objects) > 0



@then(u'text message ("{message}") must be exists in the "{chatbots}" payload')
def step_impl(context, message, chatbots):
    result = dict(context.my_object)
    for chatbot in chatbots.split(","):
        assert result.get(chatbot, None) is not None
        assert len(result.get(chatbot, None)) > 0
        if chatbot == "line":
            assert result[chatbot][0].get("type") == "text"
            assert result[chatbot][0].get("text") == message
        if chatbot == "facebook":
            assert result[chatbot][0].get("text") == message
