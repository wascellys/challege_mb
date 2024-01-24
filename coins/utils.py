from datetime import datetime
from decouple import config
import requests
from django.core.cache import cache
import locale
from django.http import Http404

HEADERS = {
    'User-Agent': 'Mozzila/5.0',
    'Accept': 'application/json'
}


def fetch_coin_info(symbol):
    cached_data = cache.get(symbol)

    if cached_data:
        return cached_data

    url = f'{config("BASE_URL_MB")}?symbol={symbol}&limit=20&offset=0&order=desc&sort=release_date'
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return {'error': 'Failed to fetch coin information'}

    data = response.json()

    if data['total_items'] == 0:
        raise Http404

    coin_data = data['response_data']['products'][0]

    price = coin_data['market_price']
    dolar_value = fetch_value_dollar()

    coin_info = {
        'coin_name': coin_data['name'],
        'symbol': coin_data['product_id'],
        'coin_price': format_currency(price),
        'coin_price_dolar': format_currency(float(price) / float(dolar_value)),
        'date_consult': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    cache_key = symbol
    cache.set(cache_key, coin_info, timeout=180)

    return coin_info


def format_currency(value, decimal_places=2, locale_currency='pt_BR.UTF-8'):
    currency = round(float(value), decimal_places)
    locale.setlocale(locale.LC_ALL, locale_currency)
    return locale.currency(currency, grouping=True, symbol=None)


def fetch_value_dollar():
    url = f"{config('BASE_URL_QUOTE')}"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        return "4.90"
    return data['USDBRL']['low']
