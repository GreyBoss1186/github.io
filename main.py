import telebot

bot = telebot.TeleBot("1435366393:AAGJhkG3y4aqrrOsU94TIUjiyE4YmZ1LwGQ")


@bot.message_handler(content_types=['text', 'audio', 'document'])
def get_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "привет! Я бот, который поможет тебе вспомнить имена учителей")

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Чтобы узнать имя учителя, просто напиши название предмета")

    elif message.text == "Математика" or message.text == "математика" or message.text == "Матеша" or message.text == "матеша":
        bot.send_message(message.from_user.id, "Иванова Галина Ивановна \nE-mail: mailmail@yandex.ru")

    elif message.text == "Русский" or message.text == "русский" or message.text == "русич" or message.text == "Русич":
        bot.send_message(message.from_user.id, "Иванова Галина Ивановна \nE-mail: mailmail@yandex.ru")

    elif message.text == "Английский" or message.text == "английский" or message.text == "англ" or message.text == "Англ" or message.text == "Английский язык" or message.text == "английский язык":
        bot.send_message(message.from_user.id, "Иванова Галина Ивановна \nE-mail: mailmail@yandex.ru")

    elif message.text == "Немецкий" or message.text == "немецкий" or message.text == "немец" or message.text == "Немец" or message.text == "Немецкий язык" or message.text == "немецкий язык":
        bot.send_message(message.from_user.id,
                         "первая группа: \nИванова Галина Ивановна \nE-mail: mailmail@yandex.ru \n \nвторая группа:\nИванова Галина Ивановна \nE-mail: mailmail@yandex.ru")

    elif message.text == "Химия" or message.text == "химия":
        bot.send_message(message.from_user.id, "Иванова Галина Ивановна \nE-mail: mailmail@yandex.ru")

    elif message.text == "Биология" or message.text == "биология" or message.text == "био" or message.text == "Био":
        bot.send_message(message.from_user.id, "Иванова Галина Ивановна \nE-mail: mailmail@yandex.ru")

    elif message.text == "География" or message.text == "география" or message.text == "гео" or message.text == "Гео":
        bot.send_message(message.from_user.id, "Иванова Галина Ивановна \nE-mail: mailmail@yandex.ru")

    elif message.text == "Физика" or message.text == "физика" or message.text == "физ" or message.text == "Физ":
        bot.send_message(message.from_user.id, "Иванова Галина Ивановна \nE-mail: mailmail@yandex.ru")

    elif message.text == "Информатика" or message.text == "информатика" or message.text == "инфа" or message.text == "инфа":
        bot.send_message(message.from_user.id, "Иванова Галина Ивановна \nE-mail: mailmail@yandex.ru")

    elif message.text == "Физкультура" or message.text == "физкультура" or message.text == "физра" or message.text == "Физра":
        bot.send_message(message.from_user.id, "Иванова Галина Ивановна \nE-mail: mailmail@yandex.ru")

    elif message.text == "История" or message.text == "история":
        bot.send_message(message.from_user.id, "Иванова Галина Ивановна \nE-mail: mailmail@yandex.ru")

    elif message.text == "Обществознание" or message.text == "обществознание" or message.text == "общество" or message.text == "Общество":
        bot.send_message(message.from_user.id, "Иванова Галина Ивановна \nE-mail: mailmail@yandex.ru")

    else:
        bot.send_message(message.from_user.id,
                         "Я не понимаю, что ты написал. Возможно, ты неправильно указал название предмета")


bot.polling(none_stop=True, interval=0)



