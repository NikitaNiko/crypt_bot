from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.keyboard_bot import main_kb
from aiogram import Router

router = Router()



@router.message(CommandStart())
async def starting(message: Message):
    print(f"ID: {message.from_user.id} -> {message.from_user.full_name} -> Chat ID:{message.chat.id}")
    await message.answer(f"Привет, {message.from_user.full_name}, \
чтобы узнать статистику отправь мне <<Статистика>>", reply_markup=main_kb)
   
