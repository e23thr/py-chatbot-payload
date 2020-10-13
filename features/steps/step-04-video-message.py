from behave import *


@when(u"(Line) an video message is added")
def step_impl(context):
    context.my_object.video_message(original_content_url=context.active_outline["original_content_url"],
                                    preview_image_url=context.active_outline["preview_image_url"],
                                    chatbot=context.active_outline["chatbots"])


@then(u'(Line) video message must have original_url = "{original_url}" and preview_url = "{preview_url}"')
def step_impl(context, original_url, preview_url):
    data = dict(context.my_object)
    chatbots = context.active_outline["chatbots"].split(",")
    for chatbot in chatbots:
        chatbot_objects = data.get(chatbot, None)
        assert chatbot_objects is not None
        assert type(chatbot_objects) is list
        assert len(chatbot_objects) == 1
        video_object = chatbot_objects[0]
        assert video_object["type"] == "video"
        assert video_object["originalContentUrl"] == original_url
        assert video_object["previewImageUrl"] == preview_url


@when(u'(Facebook) an video message is added')
def step_impl(context):
    kwargs = {"chatbot": context.active_outline["chatbots"]}
    attachment_id = context.active_outline["attachment_id"]
    url = context.active_outline["url"]
    if attachment_id != "-":
        kwargs["attachment_id"] = attachment_id
    if url != "-":
        kwargs["url"] = url
    print(kwargs)
    context.my_object.video_message(**kwargs)


@then(u'(Facebook) video message must have attachment_id = "{att_id}" and url = "{url}"')
def step_impl(context, att_id, url):
    data = dict(context.my_object)
    chatbots = context.active_outline["chatbots"].split(",")
    for chatbot in chatbots:
        chatbot_objects = data.get(chatbot, None)
        assert chatbot_objects is not None
        assert type(chatbot_objects) is list
        assert len(chatbot_objects) == 1
        image_object = chatbot_objects[0]
        assert type(image_object) is dict
        attachment_object = image_object.get("attachment", None)
        assert attachment_object is not None
        assert attachment_object.get("type", None) == "template"
        attachment_payload = attachment_object.get("payload", None)
        assert attachment_payload is not None
        assert attachment_payload.get("template_type", None) == "media"
        elements = attachment_payload.get("elements", None)
        assert type(elements) is list
        assert len(elements) == 1
        element = elements[0]
        assert element.get("media_type", None) == "video"
        if att_id != "-":
            assert element.get("attachment_id", None) == att_id
        if url != "-":
            assert element.get("url", None) == url

