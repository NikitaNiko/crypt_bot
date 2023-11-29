from aiogram.utils.keyboard import ReplyKeyboardBuilder

def coins_kb():
    items = ["ATM", "CVP", "LDO", "1INCH", "NEAR", "GAS", "Назад", "Своя монета"]

    builder = ReplyKeyboardBuilder()
    [builder.button(text= item) for item in items]
    builder.adjust(*[3] * 2)

    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

def button_gen(text: str | list):
    builder = ReplyKeyboardBuilder()

    if isinstance(text, str):
        text = [text]

    [builder.button(text=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)