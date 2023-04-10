# Generated by Django 4.2 on 2023-04-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=3)),
                ('public_key', models.CharField(max_length=42, unique=True)),
                ('private_key', models.CharField(max_length=64, unique=True)),
                ('balance', models.DecimalField(decimal_places=8, default=0, max_digits=18)),
            ],
        ),
    ]