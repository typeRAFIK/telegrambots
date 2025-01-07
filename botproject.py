import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
import logging
import random

token = dotenv_values(".env")["bot_token"]
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f"Hello, {name}")

@dp.message(Command("myinfo"))
async def echo_handler(message: types.Message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(f"Ваш id: {id}, ваше имя: {name}, ваш ник: {username}")

@dp.message(Command("random"))
async def echo_handler(message: types.Message):
    names = ["Iskender", "Arlen", "Ermek", "Beknazar", "Pdiddy", "Miles"]
    await message.answer(f"Имя: {random.choice(names)}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
