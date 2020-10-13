from behave import *


@when(u'a sticker message (package_id "{pkg_id}" sticker_id "{stk_id}") is added for "{platform}"')
def step_impl(context, pkg_id, stk_id, platform):
    context.my_object.sticker_message(package_id=pkg_id, sticker_id=stk_id)


@then(u'sticker message (package_id "{pkg_id}" sticker_id "{stk_id}") must be exists')
def step_impl(context, pkg_id, stk_id):
    data = dict(context.my_object)
    chatbots = context.active_outline['chatbots'].split(",")
    for chatbot in chatbots:
        chatbot_objects = data.get(chatbot, None)
        assert chatbot_objects is not None
        assert type(chatbot_objects) == list
        assert len(chatbot_objects) == 1
        sticker_object = chatbot_objects[0]
        assert sticker_object["type"] == "sticker"
        assert sticker_object["packageId"] == pkg_id
        assert sticker_object["stickerId"] == stk_id
