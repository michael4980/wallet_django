from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'currency', 'public_key')


class GetWallets(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'currency', 'public_key', 'balance')
