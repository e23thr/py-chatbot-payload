from behave import *


@when(u'(Facebook) an video message is added')
def step_impl(context):
    context.my_object.video_message(
        video_url=context.active_outline["url"],
        is_reusable=context.active_outline["is_reusable"] == "true",
        chat_bot="facebook"
    )


@then(u'(Facebook) video message must have url = "{url}" and is_reusable = "{is_reusable}"')
def step_impl(context, url, is_reusable):
    data = dict(context.my_object)
    chatbots = context.active_outline["chatbots"].split(",")
    for chatbot in chatbots:
        chatbot_objects = data.get(chatbot, None)
        assert chatbot_objects is not None
        assert type(chatbot_objects) == list
        obj = chatbot_objects[0]
        obj_attachment = obj.get("attachment", None)
        assert obj_attachment is not None
        assert obj_attachment.get("type", None) == "video"
        obj_payload = obj_attachment.get("payload", None)
        assert type(obj_payload.get("url", None)) == str
        assert type(obj_payload.get("is_reusable", None)) == bool
