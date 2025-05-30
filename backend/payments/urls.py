from django.urls import path

from .views import (
    GetBalanceAPIView,
    PaymentAPIView,
)

urlpatterns = [
    path("webhook/bank/", PaymentAPIView.as_view(), name="payment"),
    path(
        "organizations/<inn>/balance/", GetBalanceAPIView.as_view(), name="get-balance"
    ),
]
