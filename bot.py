from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from openweather import сurrent_weather, status_response, print_weather

from config import TOKEN

# Для передачи токена через параметр виртуального окружения
#import os
#TOKEN = os.getenv("TOKEN")


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Я Вася. Могу рассказать тебе о текущей погоде в любом городе. Набери /help, чтобы узнать как это сделать:)")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Введи название города на русском языке или на латинице, например: Москва  или Moscow")


@dp.message_handler()
async def echo_message(msg: types.Message):
    city = msg.text
    weather = print_weather(city)
    await bot.send_message(msg.from_user.id, weather)


if __name__ == '__main__':
    executor.start_polling(dp)