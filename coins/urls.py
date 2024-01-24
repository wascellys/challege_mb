from django.urls import path
from .views import CoinInfoView

urlpatterns = [
    path('coin_infos/', CoinInfoView.as_view(), name='coin_infos'),
]
