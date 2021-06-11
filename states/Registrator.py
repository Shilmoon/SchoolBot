from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    Login = State()
    Password = State()
