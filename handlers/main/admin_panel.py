from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS, sub_channels, last_messages, temp_data, \
    main_channel
from keyboards.default.main_keyboard import admins_main_keyboard
from keyboards.inline.main_keyboard import yes_no_kb, yes_no_callback
from loader import dp, bot
from states import *


@dp.message_handler(CommandStart(), user_id=ADMINS)
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!",
                         reply_markup=admins_main_keyboard)
@dp.edited_channel_post_handler()


@dp.message_handler(text='🛑 Отмена', user_id=ADMINS, state='*')
async def start_comand(message: types.Message, state: FSMContext):
    await message.delete()
    try:
        await state.finish()
    except:
        return


@dp.message_handler(text='🗑️ Удалить сообщение', user_id=ADMINS)
async def redact_post(message: types.Message):
    await message.answer(f"Введите номер сообщения, начиная с последнего")
    await DeleteMessage.number.set()


@dp.message_handler(state=DeleteMessage.number, user_id=ADMINS)
async def redact_post(message: types.Message, state: FSMContext):
    try:
        temp_data['number'] = int(message.text)-1
        await bot.forward_message(
            chat_id=message.chat.id,
            from_chat_id=main_channel,
            message_id=last_messages.data[str(main_channel)]-temp_data['number'])
        await message.answer('Удалить это сообщение?', reply_markup=yes_no_kb())
    except Exception as e:
        print(e)
        await message.answer(text='Введите корректный номер сообщения')


@dp.callback_query_handler(yes_no_callback.filter(), user_id=ADMINS,
                           state=DeleteMessage.number)
async def break_catcher(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    answer = callback_data.get('answer')

    if answer == 'yes':
        for channel_id in sub_channels.data:
            try:
                await bot.delete_message(int(channel_id), last_messages.data[channel_id] - temp_data['number'])
            except Exception as e:
                print(e)
        print(last_messages.data)
        last_messages.update_data()
        await bot.delete_message(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id - 1)
        await call.message.edit_text('Готово!')
        await state.finish()

    else:
        await call.message.delete()
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id-1)

