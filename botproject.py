import asyncio
from aiogram import Bot, Dispatcher, types

token = "8180619777:AAFh7-gj3HTMPs0EHr8YQG28fA3fXZKiFiU"
bot = Bot(token=token)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
