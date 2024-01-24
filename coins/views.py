from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import fetch_coin_info


class CoinInfoView(APIView):
    def post(self, request):
        data = request.data

        if 'symbol' not in data:
            return Response({'error': 'Symbol not provided'}, status=status.HTTP_400_BAD_REQUEST)

        symbol = data['symbol']
        coin_info = fetch_coin_info(symbol)
        return Response(coin_info, status=status.HTTP_200_OK)
