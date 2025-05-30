# Bank Payment API

REST API для приёма банковских платежей и отображения баланса организации по ИНН.
Создано с использованием Django и Django REST Framework.

---

## Требования

- Python 3.9
- Django 4.2.17
- MySQL

## Установка

1. Клонируйте или скачайте репозиторий с кодом.
2. Установите зависимости:

```bash
pip install -r requirements.txt
```
3. Создайте базу данных MySQL
4. Создайте ".env" файл
5. Внесите необходимые данные по образцу из ".env-example" в ".env"
6. Примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

**Убедитесь, что у вас активировано виртуальное окружение**.

## Эндпоинты

**`POST /webhook/bank/`**

Приём платежей.

**Пример запроса:**
```bash
{
  "operation_id": "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a",
  "amount": 145000,
  "payer_inn": "1234567890",
  "document_number": "PAY-328",
  "document_date": "2024-04-27T21:00:00Z"
}
```
Ответы:

`200 OK` — Платёж успешно зачислен или уже существует.

`400 Bad Request` — Ошибка валидации данных.

**`GET /organizations/<inn>/balance/`**

Получить баланс организации по ИНН.

**Пример запроса:**
```bash
GET /organizations/123456789012/balance/
```

**Пример ответа:**
```bash
{
  "inn": "1234567890",
  "balance": "145000.00"
}
```

## Запуск (в режиме отладки)
```bash
python manage.py runserver
```