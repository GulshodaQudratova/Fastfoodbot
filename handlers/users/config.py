from loader import dp,bot
from aiogram import types
from main import *
from keyboards.default.buttons import *
##### Click Setting Button ###############
@dp.message_handler(text=["⚙ Настройки","⚙ Sozlamalar"])
async def gotosettings(message:types.Message):
    language =language_info(message.from_user.id)
    if language=='ru':
        await message.answer(f"⚙ Добро пожаловать в раздел настроек!\n\n" 
                             f"Ð/󾓬 Вы можете изменить язык с помощью кнопок.",reply_markup=settings(language))
    else:
        await message.answer(f"⚙ Sozlamalar bo'limiga xush kelibsiz!\n\n"
                             "Ð/󾓬 Tugmachalar orqali tilni o'zgartirishingiz mumkin.",reply_markup=settings(language))
    ######### Select Language #############
@dp.message_handler(text=["Ð O'zbekcha","󾓬 Русский"])
async def change_lang(message:types.Message):
    if message.text == "Ð O'zbekcha":
        change_language(telegram_id=message.from_user.id, language="uz")
        await message.answer(f"🙂 Assalomu alaykum, {message.from_user.full_name}, @littleitalyclonebot botiga xush kelibsiz!\n\n"
                             "😋 Ushbu bot orqali mazali pitsalarga buyurtma bera olasiz. Pitsalarni manzilingizga tezkor yetkazib beramiz!\n\n" 
                             "🍕 Buyurtma berishni boshlaysizmi?", reply_markup=main_uz)
    else:
        change_language(telegram_id=message.from_user.id, language="ru")
        await message.answer(f"🙂 Ассаламу алейкум, {message.from_user.full_name}, добро пожаловать в @littleitalyclonebot bot!\n\n"
                             "😋 С помощью этого бота вы можете заказывать вкусные пиццы. Мы быстро доставим пиццу до места назначения!\n\n"
                             "🍕 Вы начинаете заказывать?", reply_markup=main_ru)
        ############ Go to Menu ##########################
    @dp.message_handler(text=["🔝 Bosh menyuga qaytish","🔝 Вернуться в главное меню"])
    async def back(message:types.Message):
        language = language_info(message.from_user.id)
        if language== "uz":
            await message.answer(f"✅ Bosh menyuga xush kelibsiz!\n"
                                 f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup=main_uz)
        else:
            await message.answer(f"✅ Добро пожаловать в главное меню!\n"
                                 f"🍕 Вкусные пиццы! Вы начинаете заказывать?",
                                 reply_markup=main_ru)
    ### Change Language Command ###############
@dp.message_handler(commands='set_language')
async def change(message:types.Message):
    language = language_info(message.from_user.id)
    if language == 'ru':
        await message.answer(f"⚙ Добро пожаловать в раздел настроек!\n\n" 
                             f"Ð/󾓬 Вы можете изменить язык с помощью кнопок.", reply_markup=settings(language))
    else:
        await message.answer("⚙ Sozlamalar bo'limiga xush kelibsiz!\n\n"
                             "Ð/󾓬 Tugmachalar orqali tilni o'zgartirishingiz mumkin.", reply_markup=settings(language))