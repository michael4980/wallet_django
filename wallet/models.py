from django.db import models

class Wallet(models.Model):
    currency = models.CharField(max_length=3)
    public_key = models.CharField(max_length=42, unique=True)
    private_key = models.CharField(max_length=128, unique=True)
    balance = models.DecimalField(max_digits=18, decimal_places=8, default=0)

