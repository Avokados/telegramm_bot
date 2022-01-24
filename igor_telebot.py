import telebot
# import cv2
from BotConfig import BotToken as bt

bot = telebot.TeleBot(bt)


@bot.message_handler(content_types=['text'])
def handle_docs_photo(message):
    print("Text recive")
    print(message)
    bot.reply_to(message, "Text poluchen")


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    print("Фото")
    try:

        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        print(file_info)
        downloaded_file = bot.download_file(file_info.file_path)

        src = '/home/alexey/TelBOT/files/' + file_info.file_path
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "Фото добавлено")
        image = cv2.imread(src)
        cv2.imshow("111", image)
    except Exception as e:
        bot.reply_to(message, e)


bot.polling(none_stop=True, interval=0)
