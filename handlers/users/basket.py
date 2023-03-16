############### About Basket ####################
from loader import dp
from aiogram import types
from main import *
from keyboards.default.buttons import *
############ See Basket ######
@dp.message_handler(text=["🛍 Мои заказы","📥 Корзина","🛍 Buyurtmalarim","📥 Savat"])
async def basket_info(message:types.Message):
    language = language_info(message.from_user.id)
    shop = shop_info(telegram_id=message.from_user.id,language=language)
    if shop==[]:
        text = "Sizning savatingiz bo'sh." if language=='uz' else "Ваша корзина пуста."
        await message.answer(text)
    else:
        text = ''
        money = " so'm" if language == 'uz' else ' сум'
        for i in shop[0]['items']:
            text += f"{i['quantity']} ✖ {i['product']}\n"
            text += ("Товары:" if language == 'ru' else "Mahsulotlar:") + str(shop[0]['all_shop']) + money + "\n"
            text += ("Доставка:" if language == 'ru' else "Yetkazib berish:") + str(17000) + money + "\n"
            text += ("Итого:" if language == 'ru' else "Jami:") + str(shop[0]['all_shop'] + 17000) + money
            await message.answer(text, reply_markup=mybasket(language=language, datas=shop[0]['items']))
    ######## Basket Query ##############
@dp.callback_query_handler(basket_callback.filter())
async def query(call:types.CallbackQuery,callback_data:dict):
    data = callback_data
    await call.answer(cache_time=60)
    language = language_info(call.from_user.id)
    if data['action'] =='order':
        shop = shop_info(telegram_id=call.from_user.id,language=language)
        if shop[0]['all_shop'] <50000:
            if language=='uz':
                await call.message.answer(f"<b>50 ming so'mdan kam buyurtmalar uchun yetkazib berish amal qilmaydi!</b>\n\n"
                                          "Buyurtmangizni filialimizdan olib ketishingiz mumkin.")
                await call.message.answer("Siz bilan bog'lanishimiz uchun telefon raqamingizni yuboring",reply_markup=getcontact(language))
            else:
                await call.message.answer("<b>Доставка не действует для заказов на сумму менее 50 тысяч сумов!</b>\n\n" 
                                          f"Вы можете забрать свой заказ в нашем отделении.")
                await call.message.answer("Отправьте нам свой номер телефона",reply_markup=getcontact(language))
        else:
            if language =='uz':
                await call.message.answer(f"🏷 Buyurtmani qabul qilish usulini tanlang:\n\n"
                                          "🛵 Yetkazib berish - restoranimizdan 5 km masofagacha yetkazib berish, pullik\n" 
                                          "k Olib ketish - restoranimizga kelib o'zingiz bilan olib ketasiz",reply_markup=gettype(language))
            else:
                    await call.message.answer("🏷 Выберите способ получения заказа:\n\n"
                                               "🛵 Доставка - до 5 км от нашего ресторана и она платная\n" 
                                               "k С собой - приходи в наш ресторан и возьми с собой",reply_markup=gettype(language))
                    await call.message.delete()
    if data['action']=='clear':
        text = "<i>Sizning savatingiz bo'sh.</i>" if language=='uz' else "Ваша корзина пуста."
        await call.message.answer(text)
        await call.message.delete()
    if data['action']=='delete':
        product = data['product']
        delete_item(telegram_id=call.from_user.id,product=product)
        shop = shop_info(telegram_id=call.from_user.id, language=language)
        if shop[0]['items'] ==[]:
            await call.message.delete()
        else:
            text = ''
            money = " so'm" if language == 'uz' else ' сум'
            for i in shop[0]['items']:
                text += f"{i['quantity']} ✖ {i['product']}\n"
                text += ("Товары:" if language == 'ru' else "Mahsulotlar:") + str(shop[0]['all_shop']) + money + "\n"
                text += ("Доставка:" if language == 'ru' else "Yetkazib berish:") + str(17000) + money + "\n"
                text += ("Итого:" if language == 'ru' else "Jami:") + str(shop[0]['all_shop'] + 17000) + money
                await call.message.edit_text(text, reply_markup=mybasket(language=language, datas=shop[0]['items']))
                if language == "uz":
                    await call.message.answer("✅ Bosh menyuga xush kelibsiz!\n"
                                              f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup=main_uz)
                else:
                    await call.message.answer(f"✅ Добро пожаловать в главное меню!\n"
                                              f"🍕 Вкусные пиццы! Вы начинаете заказывать?", reply_markup=main_ru)
    ########## Delivery Type #############
@dp.message_handler(text=['🏃 Olib ketish','🚕 Yetkazish','🏃 С собой','🚕 Доставка'])
async def next(message:types.Message):
    language = language_info(message.from_user.id)
    if language == 'uz':
        await message.answer("Siz bilan bog'lanishimiz uchun telefon raqamingizni yuboring", reply_markup=getcontact(language))
    else:
        await message.answer("Отправьте нам свой номер телефона", reply_markup=getcontact(language))