from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import registration_callback
from loader import dp, db
from aiogram import types

@dp.message_handler(Command('unregister'))
async def unregist(message: types.Message):
    if db.select_user(id = message.from_user.id) is not None:
        db.delete_user_from_db(id=message.from_user.id)
        await message.answer('Вы отписались от рассылки')
    else:
        await message.answer('Вас нет в нашей базе данных, для начала вам необходимо зарегистрироваться')

@dp.callback_query_handler(registration_callback.filter(item_name='unregister'))
async def reg_call(call: CallbackQuery):
    await call.answer(cache_time=60)
    if db.select_user(id = call.message.from_user.id) is not None:
        db.delete_user_from_db(id=call.message.from_user.id)
        await call.message.answer('Вы отписались от рассылки')
    else:
        await call.message.answer('Вас нет в нашей базе данных, для начала вам необходимо зарегистрироваться')