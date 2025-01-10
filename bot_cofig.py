from aiogram import Bot, Dispatcher
from dotenv import dotenv_values


token = dotenv_values(".env")["bot_token"]
bot = Bot(token=token)
dp = Dispatcher()
