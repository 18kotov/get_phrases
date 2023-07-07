from aiogram.fsm.state import StatesGroup, State


class TargetPhrase(StatesGroup):
    english_phrase = State()
    russian_phrase = State()
    delete = State()
