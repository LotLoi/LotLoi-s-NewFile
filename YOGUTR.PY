from telebot import TeleBot
from telebot import types
from random import randint

TOKEN = "6485736959:AAFcFcH60rtRqxMY-p6jcYFktInVJxqao7A"
bot = TeleBot(TOKEN)



kb = types.ReplyKeyboardMarkup()
btn = types.KeyboardButton("Кнопочка (Бжбжбж)")
kb.add(btn)

WBR = 101

@bot.message_handler(commands=["start"])
def handle_start(msg: types.Message):
    bot.send_message(msg.chat.id, "Го играть в розетка, пальцы, число", reply_markup=kb)
    global WBR 
    WBR = randint(1, 100)


@bot.message_handler(commands=["finish"])
def handle_finish(msg: types.Message):
    bot.send_message(msg.chat.id, "Бай бай")

@bot.message_handler(content_types=["text"])
def handle_text(msg: types.Message):
    global WBR
    text = msg.text
    if WBR == 0:
        bot.send_message(msg.chat.id, "Ноу ноу ноу, иди перезапускай литл пупсик")
    elif text.isdigit():
        text = int(text)
        if text < WBR:
            bot.send_message(msg.chat.id, "У меня больше :)))")
        if text > WBR:
            bot.send_message(msg.chat.id, "У меня меньше :(((")
        if text == WBR:
            bot.send_message(msg.chat.id, "Угадал -_-")
            
            WBR = 0
    

    if text == "Кнопочка (Бжбжбж)":
        bot.send_message(msg.chat.id, "Ты в адеквате? (Бжбжбж)")
    

print("Сервер запущен")
bot.polling()
