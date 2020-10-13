from chatbot_payload import ChatbotPayloads

p = ChatbotPayloads(chat_bots=["line","facebook"])
# print(dict(p))
p.text_message("test line", chat_bot="line")
p.text_message("test facebook", chat_bot="facebook")
# print(dict(p))
p.sticker_message("1", "2")
print(dict(p))
