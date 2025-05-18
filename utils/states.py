from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    name = State()
    dorm = State()
    room = State()

class AddEvent(StatesGroup):
    name = State()
    description = State()
    datetime = State()