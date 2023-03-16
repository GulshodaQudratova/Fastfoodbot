from aiogram import types
from loader import dp
from main import *
from keyboards.default.buttons import *
# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    language = language_info(message.from_user.id)
    text = "<i>Tushunarsiz buyruq.</i>" if language=='uz' else "<i>Непонятная команда.</i>"
    if language=='uz':
        await message.answer(text,reply_markup=main_uz)
    else:
        await message.answer(text,reply_markup=main_ru)
