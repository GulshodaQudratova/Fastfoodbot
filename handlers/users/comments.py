from aiogram.dispatcher import FSMContext
from loader import dp,bot
from aiogram import types
from keyboards.default.buttons import *
from data.config import ADMINS
from aiogram.dispatcher.filters.state import State,StatesGroup
###### State For Comment ###########
class Comment(StatesGroup):
    text = State()
    ################################### ######## Write Comment Button Type ##################
@dp.message_handler(text=["✍ Sharh qoldiring","✍ Оставить отзыв"])
async def begin(message:types.Message):
    language = language_info(message.from_user.id)
    if language=='uz':
        await message.answer("🙂 Bizga bo'lgan biror fikringiz yoki taklifingiz bo'lsa yozib qoldiring. Sizning fikringiz biz uchun fikr ingiz muhim!",reply_markup=cancel(language))
        await Comment.text.set()
    else:
        await message.answer("🙂 Если у вас есть какие-либо замечания или предложения для нас, пожалуйста, напишите их. Ваше мнение важн о для нас!",reply_markup=cancel(language))
        await Comment.text.set()
        ######### Write Comment ##############
@dp.message_handler(state=Comment.text,content_types=types.ContentType.ANY)
async def comment_get(message:types.Message,state:FSMContext):
    language = language_info(message.from_user.id)
    if message.text in ["❌ Отменить","❌ Bekor qilish"]:
        if language == "uz":
            await message.answer("✅ Bosh menyuga xush kelibsiz!\n" \
                                 f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup=main_uz)
        else:
            await message.answer(f"✅ Добро пожаловать в главное меню!\n" \
                                 f"🍕 Вкусные пиццы! Вы начинаете заказывать?", reply_markup=main_ru)
        await state.finish()
    else:
        await bot.forward_message(message_id=message.message_id,chat_id=ADMINS[0],from_chat_id=message.chat.id)
        if language == "uz":
            await message.answer("😇 Fikringiz uchun rahmat!")
            await message.answer("✅ Bosh menyuga xush kelibsiz!\n" \
                                 f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup=main_uz)
        else:
            await message.answer("😇 Спасибо за ваш отзыв!")
            await message.answer(f"✅ Добро пожаловать в главное меню!\n" \
                                     f"🍕 Вкусные пиццы! Вы начинаете заказывать?", reply_markup=main_ru)