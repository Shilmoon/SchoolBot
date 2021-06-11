from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import menu
from keyboards.inline.registkey import choice

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'''*Добро пожаловать*, я бот, который поможет вам настроить получение оценок из Электронной Школы - https://shkola.nso.ru прямо в телеграм!
Для того, чтобы получать уведолмения о новых оценках зарегистрируйтесь /register!''',parse_mode='Markdown',reply_markup=menu)

