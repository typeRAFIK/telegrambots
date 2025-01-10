from aiogram import types
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command

myinfo_router = Router()

@myinfo_router.message(Command("myinfo"))
async def echo_handler(message: types.Message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(f"Ваш id: {id}, ваше имя: {name}, ваш ник: {username}")