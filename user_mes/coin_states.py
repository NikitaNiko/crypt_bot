from aiogram import Router, F
from aiogram.types import Message
from keyboards.keyboard_bot import main_kb
from keyboards.builder import coins_kb, button_gen
from requests_bot import bitcoin
from aiogram.fsm.context import FSMContext
from utils.states import Form

router = Router()

items = ["ATM", "CVP", "LDO", "1INCH", "NEAR", "GAS", "Назад", "Своя монета"]

@router.message(F.text.lower() == "посмотреть монеты")
async def coins(message: Message, state: FSMContext):
    await state.set_state(Form.coin)
    await message.answer(f"Выбор монеты", reply_markup=coins_kb())


@router.message(Form.coin)
async def form_coin(message: Message, state: FSMContext):

    if (message.text.lower() == "Добавить монету"):
        await state.set_state(Form.your_link)
        await message.answer("Отправь ссылку на страницу с монетой:\nCite: https://coinmarketcap.com/", reply_markup=button_gen(["Назад"]))

    elif (message.text.lower() == "назад"):
        await message.answer("Ok!", reply_markup=main_kb)
        await state.clear()

    elif (message.text in items):
        if (message.text == "ATM"):
            ans = await bitcoin.price(['https://coinmarketcap.com/currencies/atletico-de-madrid-fan-token/'])
            await message.answer(ans[0], reply_markup=main_kb)

        else:
            await message.answer("Пока работает только ATM :(", reply_markup=main_kb)
        await state.clear()

    else:

        await message.answer("Такой монеты нет...")
        await state.clear()




@router.message(Form.your_link)
async def linkk(message: Message, state: FSMContext):

    if (message.text.lower() == "назад"):
        await message.answer("Ok!", reply_markup=main_kb)
        await state.clear()

    else:
        await state.update_data(your_link = message.text)
        await message.answer("Может занять некоторое время...")
        sites = await state.get_data()
        mes = await bitcoin.price([sites["your_link"]])
        await message.answer(mes[0], reply_markup=main_kb)
        await state.clear()
        
