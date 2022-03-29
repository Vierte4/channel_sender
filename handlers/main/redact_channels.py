from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS, sub_channels, last_messages, temp_data, \
    main_channel
from keyboards.default.main_keyboard import admins_main_keyboard
from keyboards.inline.main_keyboard import yes_no_kb, yes_no_callback
from loader import dp, bot
from states import *


@dp.message_handler(text='➕ Добавить канал', user_id=ADMINS)
async def redact_post(message: types.Message):
    await message.answer(f"Перечислите через запятую id всех каналов, которые вы хотите добавить")
    await RdactChannels.add.set()


@dp.message_handler(state=RdactChannels.add, user_id=ADMINS)
async def redact_post(message: types.Message, state: FSMContext):
    try:
        ids = message.text.split(',')
        ids = [int(a.strip()) for a in ids]
    except:
        await message.answer('Введите корректные id')
        return

    try:
        for id in ids:
            await bot.get_chat_administrators(id)
            print(2)
            if id not in sub_channels.data:
                sub_channels.data.append(str(id))
        print(sub_channels.data)
        sub_channels.update_data()
        await message.answer(f"Готово!")
        await state.finish()
    except Exception as e:
        print(e)
        await message.answer('Бот не является админом всех указанных каналов.'
                             'Исправьте это и попробуйте заново')
        return


@dp.message_handler(text='➖ Удалить канал', user_id=ADMINS)
async def redact_post(message: types.Message):
    await message.answer(f"Перечислите через запятую id всех каналов, которые вы хотите удалить")
    await RdactChannels.delete.set()


@dp.message_handler(state=RdactChannels.delete, user_id=ADMINS)
async def redact_post(message: types.Message, state: FSMContext):
    try:
        ids = message.text.split(',')
        ids = [(a.strip()) for a in ids]
        print(ids)
    except:
        await message.answer('Введите корректные id')
        return

    try:
        for id in ids:
            sub_channels.data.remove(id)
            last_messages.data.pop(id, None)
        sub_channels.update_data()
        last_messages.update_data()
        await message.answer(f"Готово!")
        await state.finish()
    except:
        await message.answer('Один или несколько из укаханных id не найдены.'
                             'Исправьте это и попробуйте заново')
        return


