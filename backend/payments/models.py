from django.db import models


# Create your models here.
class Organization(models.Model):
    inn = models.CharField(max_length=12, unique=True, verbose_name="ИНН организации")
    balance = models.DecimalField(
        max_digits=19, decimal_places=2, default=0, verbose_name="Баланс"
    )

    def __str__(self) -> str:
        return f"ИНН: {self.inn} — Баланс: {self.balance}"

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"


class Payment(models.Model):
    operation_id = models.UUIDField(verbose_name="ИД операции")
    amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Сумма")
    payer_inn = models.CharField(max_length=12, verbose_name="ИНН платильщика")
    document_number = models.CharField(max_length=50, verbose_name="Номер документа")
    document_date = models.DateTimeField(verbose_name="Дата документа")

    def __str__(self) -> str:
        return f"Платёж {self.operation_id}"

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"


class BalanceLog(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Сумма")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания лога"
    )

    def __str__(self) -> str:
        return f"{self.organization.inn} + {self.amount} + {self.created_at}"

    class Meta:
        verbose_name = "Лог платежа"
        verbose_name_plural = "Логи платежа"
