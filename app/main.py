import asyncio

from aiogram import Bot, Dispatcher

from app.bot.handlers.start import router
from app.core.config import settings


bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())