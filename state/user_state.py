from aiogram.fsm.state import StatesGroup, State


class user_state(StatesGroup):
    name_crypto = State()
