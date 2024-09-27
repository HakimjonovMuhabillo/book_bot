from aiogram.dispatcher.filters.state import State, StatesGroup


class Register(StatesGroup):
    name = State()
    date = State()
    time = State()
    number_of_people = State()
