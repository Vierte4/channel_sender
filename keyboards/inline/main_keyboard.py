from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

yes_no_callback = CallbackData("yes_no_callback", "answer")


def yes_no_kb():
    yes_no_kb = InlineKeyboardMarkup()

    yes_no_kb.add(
        InlineKeyboardButton(
            text='Да',
            callback_data=yes_no_callback.new(answer='yes')
        ),
        InlineKeyboardButton(
            text='Нет',
            callback_data=yes_no_callback.new(answer='no')
        )
    )

    return yes_no_kb
