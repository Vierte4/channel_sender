from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admins_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗑️ Удалить сообщение')
        ],
        [
            KeyboardButton(text='➕ Добавить канал'),
            KeyboardButton(text='➖ Удалить канал'),
        ],
        [
            KeyboardButton(text='🛑 Отмена')
        ],

    ],
    resize_keyboard=True
)
