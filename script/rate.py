import time
from xml.etree import ElementTree

import requests

def GetRate() -> float:
    """Возвращает курс доллара к рублю в момент вызова"""
    # Приведение даты в нужный формат
    current_time = time.localtime(time.time())
    
    day = str(current_time.tm_mday)
    if len(day) == 1:
        day = f'0{day}'

    month = str(current_time.tm_mon)
    if len(month) == 1:
        month = f'0{month}'
    
    # Запрос к API цб
    response = requests.get(
        f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{current_time.tm_year}')
    # Ищем нужное поле в XML
    key = 'NumCode'
    value = '840'
    for elem in ElementTree.fromstring(response.content):
        if elem.find(key).text == value:
            return float(elem.find('Value').text.replace(',','.'))
