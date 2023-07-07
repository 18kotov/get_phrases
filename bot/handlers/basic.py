import os
import time
from aiogram.types import Message
from aiogram import Router
from aiogram import F
from aiogram.filters import CommandStart, Command
from bot.handlers.states import TargetPhrase
from aiogram.fsm.context import FSMContext
from bot.utils.check_phrases import check_english_phrase, check_russian_phrase
from logic.prepare_info import get_list_phrases
from settings import get_logger

logger = get_logger(__name__)

user1 = int(os.getenv('user1'))
users = {user1}

router = Router()


@router.message(CommandStart(), F.from_user.id.in_(users))
async def get_start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}. Рад тебя видеть. Выбирай команду!')


@router.message(Command("english"), F.from_user.id.in_(users))
async def get_start(message: Message, state: FSMContext):
    logger.debug('Получена команда english')
    await message.answer('ок. добавь ключевой запрос на русском')
    # Устанавливаем пользователю состояние "добавляет строку на английском"
    await state.set_state(TargetPhrase.english_phrase)


@router.message(TargetPhrase.english_phrase, F.from_user.id.in_(users))
async def send_phrases(message: Message, state: FSMContext):
    if check_russian_phrase(message.text.lower()):
        list_phrases = get_list_phrases(message.text.lower())
        for phrase in list_phrases:
            await message.answer(phrase)
            time.sleep(0.5)
        logger.debug('Отправлен список фраз содержащих ключевое слово')
    else:
        logger.debug('Ключевое слово не прошло фильтр')
    await state.clear()


@router.message(F.from_user.id.in_(users))
async def send_info_message(message: Message):
    await message.answer('сначала выбери команду')


@router.message(~F.from_user.id.in_(users))
async def send_info_message_for_alien(message: Message):
    await message.answer('упс, тусовка только для своих!')


if __name__ == "__main__":
    pass
