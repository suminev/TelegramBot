# TelegramBot

Этот бот на запрос "Какой сегодня день?" выводит число месяца и день недели.

Для серверной части бота используется библиотека PyTelegramBotAPI (Telebot). Её нужно установить:
pip install pytelegrambotapi

После этого, указать полученный от @BotFather токен в переменную bot.
bot = telebot.TeleBot('токен');

Запустить можно на локальной машине.
python ./app.py
