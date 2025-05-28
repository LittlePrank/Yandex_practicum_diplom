# Дарья Плотникова, 30-я когорта - Финальный проект. Инженер по тестированию плюс
import configuration    
import requests
import data 

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=data.order_body)

def get_order_by_numder(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_NUMBER, params = {'t':track_number})
