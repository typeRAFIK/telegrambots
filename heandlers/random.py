from aiogram import types
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
import random

random_router = Router()
@random_router.message(Command("random"))
async def echo_handler(message: types.Message):
    names = ["Iskender", "Arlen", "Ermek", "Beknazar", "Pdiddy", "Miles"]
    await message.answer(f"Имя: {random.choice(names)}")