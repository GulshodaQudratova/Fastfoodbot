from loader import dp,bot
from aiogram import types
from keyboards.default.buttons import *
from main import *
from data.config import ADMINS
from aiogram.dispatcher import FSMContext
@dp.message_handler(content_types=types.ContentType.CONTACT,is_sender_contact=True)
async def get_contact(message:types.Message,state:FSMContext):
    telegram_id = message.from_user.id
    contact = message.contact.phone_number
    language = language_info(telegram_id)
    await state.update_data(
        {'level': 'category'}
    )
    change_phone(telegram_id=message.from_user.id,phone=contact)
    text = "⬇ To'lov qilish usulini tanlang" if language=='uz' else " Выберите способ оплаты"
    await message.answer(text,reply_markup=payment(language))
@dp.message_handler(text=["Naqd","Click","Наличные"])
async def payment_send(message:types.Message):
    language = language_info(message.from_user.id)
    text = "Bot Test Rejimda Ishlayapti" if language=='uz' else "Бот работает в тестовом режиме"
    await message.answer(text=text)
    if language == "uz":
        await message.answer("✅ Bosh menyuga xush kelibsiz!\n"
                             f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup=main_uz)
    else:
        await message.answer(f"✅ Добро пожаловать в главное меню!\n" 
                             f"🍕 Вкусные пиццы! Вы начинаете заказывать?", reply_markup=main_ru)
    shop = shop_info(telegram_id=message.from_user.id, language=language)
    text = ''
    payment_type = message.text
    user_info = all_info(message.from_user.id)
    link =f"https://t.me/{user_info['phone']}"
    user= f"👤 {user_info['name']}\n" \
          f"💬 <a href='{link}'>Telegram</a>\n"
    text += user+'\n'+payment_type + '\n'
    money = " so'm" if language == 'uz' else ' сум'
    for i in shop[0]['items']:
        text += f"{i['quantity']} ✖ {i['product']}\n"
    text += ("Товары:" if language == 'ru' else "Mahsulotlar:") + str(shop[0]['all_shop']) + money + "\n"
    text += ("Доставка:" if language == 'ru' else "Yetkazib berish:") + str(17000) + money + "\n"
    text += ("Итого:" if language == 'ru' else "Jami:") + str(shop[0]['all_shop'] + 17000) + money
    await bot.send_message(chat_id=ADMINS[0],text=text)
