from chatbot_payload import ChatbotPayloads

p = ChatbotPayloads(chat_bots=["line", "facebook"])
# print(dict(p))
# p.text_message("test line", chat_bot="line")
# p.text_message("test facebook", chat_bot="facebook")
# print(dict(p))
# p.sticker_message("1", "2")
# p.image_message(chatbot="line", original_content_url="https://original_content_url", preview_image_url="https://preview_image_url")
# p.image_message(chatbot="facebook", attachment_id="123")
p.image_message(chatbot="facebook", url="https://test-url")
print(dict(p))

