from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Помощь')

        ],
        [
            KeyboardButton(text='Зарегистрироваться')
        ]
    ],
    resize_keyboard=True

)