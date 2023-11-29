from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Статистика")
        ],
        [
            KeyboardButton(text="Посмотреть монеты"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)