import telebot;
from datetime import datetime;

bot = telebot.TeleBot('токен');
@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == "Какой сегодня день?":
        currentNumber = datetime.now().strftime('%A')
        currentDay = datetime.now().day
        bot.send_message(message.from_user.id, f"Число: {currentDay}, день: {currentNumber}")
    else:
        bot.send_message(message.from_user.id, "Спроси, какой сегодня день!")

bot.polling(none_stop=True, interval=0)