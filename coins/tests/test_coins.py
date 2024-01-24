import locale
import django
import os

import pytest

from coins.utils import format_currency

os.environ['DJANGO_SETTINGS_MODULE'] = "core.settings"
django.setup()

from rest_framework import status
from rest_framework.test import APIClient

URL = 'https://store.mercadobitcoin.com.br/api/v1/marketplace/product/unlogged'


@pytest.fixture
def api_client():
    return APIClient()


def test_coin_info_view_200(api_client):
    data = {
        "symbol": "BTC"
    }
    response = api_client.post(f'/coin_infos/', data=data, format='json')
    assert response.status_code == status.HTTP_200_OK


def test_coin_info_view_404(api_client):
    data = {
        "symbol": "BTCAAA"
    }
    response = api_client.post(f'/coin_infos/', data=data, format='json')
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_coin_info_view_400(api_client):
    data = {}
    response = api_client.post(f'/coin_infos/', data=data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_format_currency():
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    result = format_currency(50000.6789)
    assert result == '50.000,68'
