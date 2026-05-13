import asyncio

from aiogram import Bot, Dispatcher

from app.bot.handlers.start import router
from app.core.config import settings
from app.db.session import init_db


bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

dp.include_router(router)


async def main():
    await init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())