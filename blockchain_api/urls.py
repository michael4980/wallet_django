from django.urls import path
from wallet.views import homepage, get_wallets, create_eth_wallet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('api/v1/wallets/create', create_eth_wallet, name='wallet-create'),
    path('', homepage, name='homepage'),
    path('api/v1/wallets/list', get_wallets, name='wallet-list'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
