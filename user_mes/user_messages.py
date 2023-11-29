from aiogram import Router, F
from aiogram.types import Message
from keyboards.keyboard_bot import main_kb
from keyboards.builder import coins_kb
from requests_bot import bitcoin

router = Router()

@router.message(F.text.lower() == "статистика")
async def stat(message: Message):
    await message.answer("Может занять до 30 секунд!")
    info = await bitcoin.getting()
    await message.answer(f"{info}", reply_markup=main_kb)


