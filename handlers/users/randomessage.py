from loader import dp
from aiogram import types

@dp.message_handler()
async def noname(message: types.Message):
    await message.answer('Я не совсем вас понимаю, напишите /help для того чтобы просмотреть список комманд')