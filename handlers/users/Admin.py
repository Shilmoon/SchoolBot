from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from data.config import admins
from loader import dp, db, bot
from aiogram import types

from states import Send


@dp.message_handler(Command('GetUsers'))
async def admin_message(message: types.Message):
    if message.from_user.id in admins:
        users  = db.select_all()
        users1 = ''
        for  i in users:
            print(i[0],i[1],i[2])
            users1 += str([i[0],i[1],i[2]]) + '\n'

        await message.answer(users1)

@dp.message_handler(Command('sendmessage'))
async def sending(message: types.Message):
    if message.from_user.id in admins:
        await message.answer('Отправьте id пользователя')
        await Send.Sends.set()


@dp.message_handler(state=Send.Sends)
async def sending(message: types.Message, state: FSMContext):
    await state.update_data(userid= message.text)
    await message.answer('Отправьте текст сообщения')
    await Send.Text.set()

@dp.message_handler(state=Send.Text)
async def sending(message: types.Message, state: FSMContext):
    data = await state.get_data()
    userid = data.get('userid')
    try:
        await bot.send_message(userid,message.text)
        await message.answer('Сообщение успешно отправлено')
    except Exception as e:
        await message.answer('Сообщение не отпрвлено произошла ошибка')
    await state.finish()
