from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.buttons import *
from loader import dp
from main import *
from states.language import Language
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    check = create(name=full_name, telegram_id=telegram_id)
    if check == 400:
        language = language_info(telegram_id)
        if language == 'uz':
            await message.answer(f"✅ Bosh menyuga xush kelibsiz!\n"
                                 f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup = main_uz)
        else:
            await message.answer(f"✅ Добро пожаловать в главное меню!\n"
                                 f"🍕 Вкусные пиццы! Вы начинаете заказывать?", reply_markup = main_ru)
    else:
        await message.answer(f"🇺🇿 Botdan foydalanish uchun o'zingizga qulay tilni tanlang.\n" 
                             f"󾓬 Выберите удобный для вас язык для использования бота.", reply_markup = choose_language)
        create(full_name, telegram_id=telegram_id)
        await Language.language.set()
@dp.message_handler(state=Language.language)
async def set_language_system(message:types.Message,state:FSMContext):
    if message.content_type =='text':
        if message.text in ["🇺🇿 O'zbekcha","󾓬 Русский"]:
            if message.text == "🇺🇿 O'zbekcha":
                change_language(telegram_id=message.from_user.id, language="uz")
                await message.answer("✅ Bosh menyuga xush kelibsiz!\n"
                                     f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup=main_uz)
            else:
                change_language(telegram_id=message.from_user.id, language="ru")
                await message.answer(f"✅ Добро пожаловать в главное меню!\n"
                                 f"🍕 Вкусные пиццы! Вы начинаете заказывать?", reply_markup=main_ru)
            await state.finish()
        else:
            await message.answer(f"🇺🇿 Botdan foydalanish uchun o'zingizga qulay tilni tanlang.\n"
                                 f"󾓬 Выберите удобный для вас язык для использования бота.", reply_markup=choose_language)
            await Language.language.set()
    else:
        await message.answer(f"🇺🇿 Botdan foydalanish uchun o'zingizga qulay tilni tanlang.\n"
                             f"󾓬 Выберите удобный для вас язык для использования бота.", reply_markup=choose_language)
        await Language.language.set()