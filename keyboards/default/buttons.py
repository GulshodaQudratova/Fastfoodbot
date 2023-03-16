from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from main import *
from aiogram.utils.callback_data import CallbackData
basket_callback = CallbackData('mykb','action','product')
callback = CallbackData('ikb', 'action', 'count', 'product')
choose_language = ReplyKeyboardMarkup(resize_keyboard=True)
choose_language.insert(KeyboardButton(text="🇺🇿 O'zbekcha")).insert(KeyboardButton(text="󾓬 Русский"))
main_uz = ReplyKeyboardMarkup(resize_keyboard=True)
main_uz.row(KeyboardButton(text="🍴 Menyu")).row( KeyboardButton(text="🛍 Buyurtmalarim"),KeyboardButton(text="📥 Savat") ).row(KeyboardButton(text="✍ Sharh qoldiring"),KeyboardButton(text="⚙ Sozlamalar"))
main_ru = ReplyKeyboardMarkup(resize_keyboard=True)
main_ru.row(KeyboardButton(text="🍴 Меню")).row(KeyboardButton(text="🛍 Мои заказы"),
                                               KeyboardButton(text="📥 Корзина") ).row(KeyboardButton(text="✍ Оставить отзыв"),
                                                                                      KeyboardButton(text="⚙ Настройки"))
########## Categories Button ##############
def categories(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    if language=='uz':
        button.row(KeyboardButton(text="⬅ Orqaga"),
                   KeyboardButton(text="📥 Savat"))
    if language =='ru':
        button.row(KeyboardButton(text="⬅ Назад"),
                   KeyboardButton(text="📥 Корзина"))
    datas = get_categories(language)
    for data in datas:
        button.insert(KeyboardButton(text=data))
        return button
    # category bosilgan: yo subcategory yo productlar chiqadi
def product_or_subcategory(category,language,product=None):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    data = category_info(language=language,category=category)
    if 'subcategory' in data:
        button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if language == 'uz':
        button.row(KeyboardButton(text="⬅ Orqaga"),
                   KeyboardButton(text="📥 Savat"))
    if language == 'ru':
        button.row(KeyboardButton(text="⬅ Назад"),
                   KeyboardButton(text="📥 Корзина"))
        datas = data['subcategory']
        for data in datas:
            button.insert(KeyboardButton(text=f"🍽 {data}"))
            return button
    else:
        button = InlineKeyboardMarkup()
        data = data['products']
        if len(data)>1:
            for i in data[1:]:
                button.add(InlineKeyboardButton(text=f"{i['name']} {i['price']}", callback_data=callback.new(action="next",product=i['id'])),
        button.row(InlineKeyboardButton(text="-",callback_data=callback.new(action="decrease",count=1,product=product)) ,
                            InlineKeyboardButton(text="1",callback_data="1"),
                            InlineKeyboardButton(text="+",callback_data=callback.new(action="increase",count=1,product=product))))
        if language=='ru':
            button.add(InlineKeyboardButton(text="📥 Добавить в корзину",callback_data=callback.new(action="add",count=1,product=product)))
        else:
            button.add(InlineKeyboardButton(text="📥 Savatga qo'shish",callback_data=callback.new(action="add",count=1,product=product)))
        return button
    ############ Product #################################
def to_product(language,product,count):
    button = InlineKeyboardMarkup()
    button.row(InlineKeyboardButton(text="-", callback_data=callback.new(action="decrease", count=count, product=product)) ,
               InlineKeyboardButton(text=f"{count}", callback_data=count),
               InlineKeyboardButton(text="+", callback_data=callback.new(action="increase", count=count, product=product)))
    if language == 'ru':
        button.add(InlineKeyboardButton(text="📥 Добавить в корзину", callback_data=callback.new(action="add", count=count, product=product)))
    else:
        button.add(InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data=callback.new(action="add", count=count, product=product)))
    return button
    ############# Button Setting #################
def settings(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    button.row(InlineKeyboardButton(text="Ð O'zbekcha"),
               InlineKeyboardButton(text="󾓬 Русский"))
    if language=='uz':
        button.add(InlineKeyboardButton(text="🔝 Bosh menyuga qaytish"))
    else:
        button.add(InlineKeyboardButton(text="🔝 Вернуться в главное меню"))
        return button
    ############## Button Comment #########
def cancel(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    if language=='ru':
        button.add(KeyboardButton(text="❌ Отменить"))
    else:
        button.add(KeyboardButton(text="❌ Bekor qilish"))
        return button
        ######### Button Basket #######
def mybasket(language,datas):
    button = InlineKeyboardMarkup()
    if language=='uz':
        button.row(InlineKeyboardButton(text="🗑 Savatni tozalash",callback_data=basket_callback.new(action='clear',product=0)),InlineKeyboardButton(text="🚖 Hisob-kitob", callback_data=basket_callback.new(action='order', product=0)))
    else:
        button.row(InlineKeyboardButton(text="🗑 Очистить корзину", callback_data=basket_callback.new(action='clear', product=0)),
                            InlineKeyboardButton(text="🚖 Оформить заказ", callback_data=basket_callback.new(action='order', product=0)))
        for data in datas:
            button.add(InlineKeyboardButton(text=f"❌ {data['product']}",callback_data=basket_callback.new(action='delete',product=data['produc return button '])))
        return button
############## Get Contact ###########3
def getcontact(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    if language == 'uz':
        button.add(KeyboardButton(text="📞 Telefon raqamimni jo'natish",request_contact=True))
        button.add(KeyboardButton(text="❌ Bekorqilish"))
    else:
        button.add(KeyboardButton(text="📞 Поделитесь мои мномером телефона",request_contact=True))
        button.add(KeyboardButton(text="❌ Отменить"))
    return button
########### Product #################
def product_button(data,language):
    button = InlineKeyboardMarkup()
    product = data[0]['id']
    if len(data) > 1:
        for i in data[1:]:
            button.add(InlineKeyboardButton(text=f"{i['name']}{i['price']}",
                                            callback_data=callback.new(action="next", product=i['id'], count=1)))
            button.row(InlineKeyboardButton(text=" - ", callback_data=callback.new(action="decrease", count=1, product=product)) ,
                       InlineKeyboardButton(text="1", callback_data="1"),
                       InlineKeyboardButton(text=" + ", callback_data=callback.new(action="increase", count=1, product=product)))
    if language == 'ru':
        button.add(InlineKeyboardButton(text="📥 Добавитьвкорзину", callback_data=callback.new(action="add", count=1, product=product)))
    else:
        button.add(InlineKeyboardButton(text="📥 Savatgaqo'shish", callback_data=callback.new(action="add", count=1, product=product)))
    return button
def payment(language):
        button = ReplyKeyboardMarkup(resize_keyboard=True)
        if language=='uz':
            button.add("Naqd")
            button.add("Click")
            button.row(KeyboardButton(text="⬅ Orqaga"),
                       KeyboardButton(text="❌ Bekor qilish"))
        else:
            button.add("Наличные")
            button.add("Click")
            button.row(KeyboardButton(text="⬅ Назад"),
                       KeyboardButton(text="❌ Отменить"))
        return button
############ Get Location ################
def mylocation(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    if language == 'uz':
        button.add(KeyboardButton(text="📍 Manzilni yuborish", request_location=True))
        button.add(KeyboardButton(text="❌ Bekor qilish"))
    else:
        button.add(KeyboardButton(text="📍 Адрес доставки", request_location=True))
        button.add(KeyboardButton(text="❌ Отменить"))
        return button
##### Get Product Type #############
def gettype(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    if language == 'uz':
        button.add(KeyboardButton(text="🏃 Olib ketish"))
        button.add(KeyboardButton(text="🚕 Yetkazish"))
        button.add(KeyboardButton(text="❌ Bekor qilish"))
    else:
        button.add(KeyboardButton(text="🏃 С собой"))
        button.add(KeyboardButton(text="🚕 Доставка"))
        button.add(KeyboardButton(text="❌ Отменить"))
        return button