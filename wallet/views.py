from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Wallet
from .serializers import WalletSerializer, GetWallets
from .utils import create_wallet
from drf_spectacular.utils import extend_schema

def homepage(request):
    '''welcome page'''
    return render(request, 'homepage.html')

@extend_schema(
    description='Get list of all wallets',
    responses={200: GetWallets},
)
@api_view(['GET'])
def get_wallets(request):
    '''get list of all wallets'''
    wallets = Wallet.objects.all()
    serializer = GetWallets(wallets, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@extend_schema(
    description='Create new wallet with structured response',
    request=WalletSerializer,
    responses={201: WalletSerializer},
)
@api_view(['POST'])
def create_eth_wallet(request):
    '''create new wallet with structured response'''
    data = request.data
    if 'currency' not in data or data['currency'] != 'ETH':
        return Response({'error': 'Invalid request data. Currency should be "ETH".'}, status=status.HTTP_400_BAD_REQUEST)
    result = create_wallet()
    wallet = Wallet.objects.get(id=result)
    serializer = WalletSerializer(wallet)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

