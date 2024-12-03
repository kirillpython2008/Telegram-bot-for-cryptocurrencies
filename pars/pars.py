import requests

url_binance = 'https://api.binance.com/api/v3/ticker/price'
url_cb = 'https://www.cbr-xml-daily.ru/daily_json.js'


def return_price_crypto(cryptocurrency):
    price = requests.get(url_binance).json()
    for i in price:
        if i['symbol'] == cryptocurrency:
            return str(i['price'])[:-6]


def return_price_dollar():
    dollar = requests.get(url_cb).json()

    return str(dollar["Valute"]["USD"]["Value"])[:-2]


def return_price_euro():
    euro = requests.get(url_cb).json()

    return str(euro["Valute"]["EUR"]["Value"])[:-2]
