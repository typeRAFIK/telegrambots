import asyncio
import logging
from bot_cofig import bot, dp
from heandlers import (myinfo,
                       random,
                       start)
from heandlers import book_catalog
from heandlers import complaint_dialog

async def main():
    dp.include_router(myinfo.myinfo_router)
    dp.include_router(random.random_router)
    dp.include_router(book_catalog.catalog_router)
    dp.include_router(start.start_router)
    dp.include_router(complaint_dialog.complaint_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
