import asyncio
import logging
from bot_cofig import bot, dp
from heandlers import (myinfo,
                       random,
                       start)

async def main():
    dp.include_router(myinfo.myinfo_router)
    dp.include_router(random.random_router)
    dp.include_router(start.start_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
