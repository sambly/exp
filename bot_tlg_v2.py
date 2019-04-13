# -*- coding: utf-8 -*-
token="843678390:AAHGey2kE0Bj-EyLn-CHPCQfk8ehxjTw5fA"




import telebot

#proxy={"https":"https://104.248.89.208:8080"}
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! I am HabrahabrExampleBot. How can i help you?")
    
    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")
    
    else:
        bot.send_message(message.from_user.id, "Sorry, i dont understand you.")

bot.polling(none_stop=True, interval=0)

