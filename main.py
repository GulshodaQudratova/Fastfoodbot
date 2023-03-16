import requests
BASE_URL = 'http://127.0.0.1:8000'
import json
####### User All Info #########
def all_info(telegram_id):
    response = requests.post(f"{BASE_URL}/en/api/botuser/",data={'telegram_id':telegram_id})
    data = json.loads(response.text)
    return data
    ################## Language Info ######################
def language_info(telegram_id):
    response = requests.post(f"{BASE_URL}/en/api/botuser/", data={'telegram_id': telegram_id})
    data = json.loads(response.text)
    print(response)
    print(data)
    return data['language']
    ###################### Get All Categories ##############
def get_categories(language):
    response = requests.get(f"{BASE_URL}/{language}/api/category/")
    data = json.loads(response.text)
    categories = [i['name'] for i in data]
    return categories
    ######### Get bot russian and uzbek categories ###############
def get_all_categories():
    response = requests.get(f"{BASE_URL}/en/api/category/")
    data = json.loads(response.text)
    category_uz = [i['name_uz'] for i in data]
    category_ru = [i['name_ru'] for i in data]
    return category_ru+category_uz
    ############# Get Search Category ###################
def category_info(language,category):
    response = requests.get(f"{BASE_URL}/{language}/api/category/?search={category}")
    data = json.loads(response.text)
    data = data[0]
    if data['subcategory'] ==[]:
        categories = []
        for i in data['products']:
            data = {}
            data['id'] = i['id']
            data['name'] = i['name']
            data['price'] = i['price']
            data['image'] = i['image']
            categories.append(data)
        info = {'products':categories}
    else:
        categories = [i['name'] for i in data['subcategory']]
        info = {'subcategory': categories}
        return info
        ############# SubCategory ##########
def subcategory_info(language,subcategory):
    response = requests.get(f"{BASE_URL}/{language}/api/subcategory/?search={subcategory}")
    data = json.loads(response.text)
    return data[0]['products']
    ######### Get Product #####################
def get_product(id,language):
    response = requests.get(f"{BASE_URL}/{language}/api/product/{id}/")
    data = json.loads(response.text)
    return data
    ########## Create User #################
def create(name,telegram_id):
    response = requests.post(f"{BASE_URL}/en/api/botuser/",data={"name":name,"telegram_id":telegram_id})
    return response.status_code
    ############ Change Language ##################
def change_language(telegram_id,language):
    response = requests.post(f'{BASE_URL}/en/api/change/',data={'telegram_id':telegram_id,'language':language})
    return response.status_code
    ########### Change Phone Number ##################
def change_phone(telegram_id,phone):
    response = requests.post(f'{BASE_URL}/en/api/phone/',data={'telegram_id':telegram_id,'phone':phone})
    return response.status_code
    ################ Shop Info ##################
def shop_info(telegram_id,language):
    response = requests.post(f'{BASE_URL}/{language}/api/shop/',data={'telegram_id':telegram_id})
    data = json.loads(response.text)
    return data
    ############# Set Order ##################
def set_order(telegram_id,product,quantity):
    response = requests.post(f'{BASE_URL}/en/api/set_order/',data={'telegram_id':telegram_id,'product':product,'quantity':quantity})
    data = json.loads(response.text)
    return data
    ############## Delete Basket ##################
def delete_basket(telegram_id):
    response = requests.post(f'{BASE_URL}/en/api/delete_basket/',data={'telegram_id':telegram_id})
    data = json.loads(response.text)
    return data
    ########### Delete Item ##################
def delete_item(telegram_id,product):
    response = requests.post(f'{BASE_URL}/en/api/delete_item/',data={'telegram_id':telegram_id})
    data = json.loads(response.text)
    return data