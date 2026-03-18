import requests
from celery import shared_task
from .models import Currency, RateHistory


@shared_task
def update_currency_rates():
    url = "https://api.monobank.ua/bank/currency"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return f"Помилка API: {response.status_code}"
    except Exception as e:
        return f"Помилка запиту: {str(e)}"

    data = response.json()

    # 1. Отримуємо всі валюти, які зараз на моніторингу (is_active=True)
    # Створюємо словник {iso_code: об'єкт_валюти} для швидкого пошуку
    active_currencies = {c.iso_code: c for c in Currency.objects.filter(is_active=True)}

    if not active_currencies:
        return "Немає активних валют для моніторингу"

    updated_count = 0

    # 2. Проходимо по всьому списку від Monobank
    for item in data:
        # Перевіряємо, чи це курс до гривні (980)
        if item.get("currencyCodeB") == 980:
            iso_a = item.get("currencyCodeA")

            # 3. Перевіряємо, чи є ця валюта в нашому списку активних
            if iso_a in active_currencies:
                currency_obj = active_currencies[iso_a]

                # Monobank дає або rateBuy (купівля), або rateCross (для менш популярних)
                rate_value = item.get("rateBuy") or item.get("rateCross")

                if rate_value:
                    RateHistory.objects.create(
                        currency=currency_obj,
                        rate=rate_value
                    )
                    updated_count += 1

    return f"Оновлено курсів: {updated_count}"