from aiogram.dispatcher.filters.state import StatesGroup, State

class DeleteMessage(StatesGroup):
    number = State()

class RdactChannels(StatesGroup):
    add = State()
    delete = State()