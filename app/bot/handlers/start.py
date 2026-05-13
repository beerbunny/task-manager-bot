from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.db.session import async_session_maker
from app.services.user_service import UserService


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    async with async_session_maker() as session:
        service = UserService(session)
        user, created = await service.get_or_create_user(message.from_user)

    if created:
        await message.answer("Ты зарегистрирован в Task Manager ✅")
    else:
        await message.answer("Ты уже есть в базе. Task Manager готов ✅")