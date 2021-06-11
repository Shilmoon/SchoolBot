import json

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text

from loader import dp, db
from aiogram import types

import requests

from states import Test

@dp.message_handler(Command('register'))
async  def registing(message: types.Message):
    user = db.select_user(message.from_user.id)
    if user is None:
        await message.answer('Отлично, введите *логин*',parse_mode='Markdown')
        await Test.Login.set()
    else:
        await message.answer('Вы уже зарегестрированы')


@dp.message_handler(text='Зарегистрироваться')
async  def registing(message: types.Message):
    user = db.select_user(message.from_user.id)
    if user is None:
        await message.answer('Отлично, введите *логин*', parse_mode='Markdown')
        await Test.Login.set()
    else:
        await message.answer('Вы уже зарегестрированы')

@dp.message_handler(state=Test.Login)
async def login(message: types.Message,state: FSMContext):
    login = message.text

    await state.update_data(login=login)
    await Test.next()
    await message.answer('Теперь введите *пароль*',parse_mode='Markdown')

@dp.message_handler(state=Test.Password)
async def password(message: types.Message,state: FSMContext):
    data  = await state.get_data()
    login = data.get('login')
    password = message.text
    payload = {'login_login': login, 'login_password': password}
    try:
        with requests.session() as s:
            s.post('https://shkola.nso.ru/auth/login', data=payload)
            s.get('https://shkola.nso.ru/actions/snils_checker/fill?no-input')
            f = s.get('https://shkola.nso.ru/api/ProfileService/GetPersonData')
        f = (json.loads(f.text))['user_fullname']
        await message.answer(f'Вы успешно зарегестрировались как пользователь {f}, теперь уведомления об оценках будут приходить в этот чат')
        db.add_user_to_Db(id=message.from_user.id, login_login=login, login_password=password)
    except Exception:
        await message.answer('Вы указали неправильные данные, попробуйте зарегестрироваться снова')
    await state.finish()



