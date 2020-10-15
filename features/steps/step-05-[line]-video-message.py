from behave import *


@when(u"(Line) an video message is added")
def step_impl(context):
    print("VIDEO URL: ", context.active_outline["original_content_url"])
    context.my_object.video_message(video_url=context.active_outline["original_content_url"],
                                    preview_url=context.active_outline["preview_image_url"],
                                    chat_bot="line")


@then(u'(Line) video message must have original_url = "{original_url}" and preview_url = "{preview_url}"')
def step_impl(context, original_url, preview_url):
    data = dict(context.my_object)
    chatbots = context.active_outline["chatbots"].split(",")
    for chatbot in chatbots:
        chatbot_objects = data.get(chatbot, None)
        assert chatbot_objects is not None
        assert type(chatbot_objects) is list
        assert len(chatbot_objects) == 1
        image_object = chatbot_objects[0]
        assert image_object["type"] == "video"
        assert image_object["originalContentUrl"] == original_url
        assert image_object["previewImageUrl"] == preview_url
