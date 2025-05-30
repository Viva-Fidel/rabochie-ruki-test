from django.db import transaction
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BalanceLog, Organization, Payment
from .serializers import GetBalanceSerializer, PaymentSerializer


# Create your views here.
class PaymentAPIView(APIView):
    def post(self, request: Request) -> Response:
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        operation_id = data["operation_id"]

        # Если такой платёж есть, возвращаем 200 с комментарием
        if Payment.objects.filter(operation_id=operation_id).exists():
            return Response(
                {"detail": f"Платёж c ид {operation_id} уже был зачислен"},
                status=status.HTTP_200_OK,
            )

        with transaction.atomic():
            payment = serializer.save()

            # Находим или создаем организацию, если такой нет в БД
            org, _ = Organization.objects.get_or_create(inn=payment.payer_inn)

            # Начисляем баланс
            org.balance += payment.amount
            org.save()

            # Сохраняем лог
            BalanceLog.objects.create(
                organization=org,
                amount=payment.amount,
            )

            print(f"Поступил платёж от ИНН {org.inn} на сумму {payment.amount}")

        return Response({"detail": "Платёж сохранён"}, status=status.HTTP_200_OK)


class GetBalanceAPIView(generics.RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = GetBalanceSerializer
    lookup_field = "inn"
