import fileinput

from aiogram.dispatcher import Dispatcher
from aiogram.types.base import InputFile
from aiogram.utils import executor
from aiogram import Bot
from aiogram import types
from BotConfig import BotToken as bt
import io
import os

import cv2
import numpy as np

bot = Bot(token=bt)
dp = Dispatcher(bot)
image = io.BytesIO()

@dp.message_handler(commands=["start"])
async def start_message(message):
    start_text = 'Здравствуйте, пришлите фото для обработки.'
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text=start_text)


@dp.message_handler(content_types=['photo'])
def handle_photo(message):
    chat_id = message.chat.id
    print(chat_id)
    a = int(0)
    print("a = " + str(a))
    a = a + 1
    message.photo[-1].download(str(chat_id))
    n_img = cv2.imread(str(chat_id))
    n_img = cv2.GaussianBlur(n_img, (5, 5), 3)
    n_img = cv2.cvtColor(n_img, cv2.COLOR_BGR2GRAY)
    n_img = cv2.Canny(n_img, 30, 30)
    kernel = np.ones((3, 3), np.uint8)
    n_img = cv2.dilate(n_img, kernel, iterations=1)
    path = ''
    cv2.imwrite(os.path.join(path, 'n_img.jpg'), n_img)
    bot.send_photo(chat_id=chat_id, photo='waka.jpg')







# @dp.message_handler(content_types=["photo"])
# async def photo_handler(message: types.Message):
#     image.write(message.document.thumb.download(destination=image))
#     chat_id = message.chat.id
#     await bot.send_photo(chat_id=chat_id, photo=image)
# Вывод байт-обьекта
# print(image.getvalue())

# тип данных в переменной - io.BytesIO
# await message.answer(type(image))




if __name__ == '__main__':
    executor.start_polling(dp)
