from aiogram import Router, F, types
from aiogram.filters import Command
start_router = Router()
@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    # message.from_user.id
    # await message.answer(f"Привет, {name}")
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us"),
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data="takecomplaint")
            ],
            [
                types.InlineKeyboardButton(text="Наш каталог", callback_data="book_katalog")
            ],
            [
                types.InlineKeyboardButton(text="Реклама", callback_data="advertising")
            ]
        ]
    )
    await message.answer(f"Привет, {name}", reply_markup=kb)


@start_router.callback_query(F.data == "about_us")
async def about_us_handler(callback: types.CallbackQuery):
    # await callback.answer("Мы - магазин книг")
    await callback.message.answer("Мы - магазин книг")

@start_router.callback_query(F.data == "takecomplaint")
async def take_complaint_handler(callback: types.CallbackQuery):
    await callback.message.answer("пишите вашу жалобу")