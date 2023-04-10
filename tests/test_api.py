from django.test import TestCase, Client
from unittest.mock import patch
from rest_framework import status
from wallet.models import Wallet
from wallet.utils import create_wallet


class WalletTests(TestCase):

    def setUp(self):
        self.client = Client()

    @patch('wallet.views.create_wallet')
    def test_create_eth_wallet(self, mock_create_wallet):
        mock_create_wallet.return_value = 1
        response = self.client.post('/api/v1/wallets/create', {'currency': 'ETH'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['id'], 1)

    def test_create_eth_wallet_with_invalid_currency(self):
        response = self.client.post('/api/v1/wallets/create', {'currency': 'BTC'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid request data. Currency should be "ETH".')

    @patch('wallet.views.Wallet.objects.all')
    def test_get_wallets(self, mock_wallets):
        mock_wallets.return_value = [Wallet(private_key='test_private_key')]
        response = self.client.get('/api/v1/wallets/list')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
