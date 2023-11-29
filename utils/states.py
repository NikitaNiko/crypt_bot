from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    coin = State()
    your_link = State()