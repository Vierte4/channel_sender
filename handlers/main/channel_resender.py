from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import main_channel, sub_channels, last_messages
from loader import dp, bot


@dp.channel_post_handler(chat_id=main_channel, content_types=types.ContentTypes.ANY)
async def bot_help(message: types.Message):
    last_messages.data[str(main_channel)] = message.message_id
    for channel_id in sub_channels.data:
        copy = await message.send_copy(chat_id=int(channel_id))
        last_messages.data[channel_id]=copy.message_id
    print(last_messages.data)
    last_messages.update_data()