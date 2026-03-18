from django.contrib import admin
from .models import Currency, RateHistory

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('code', 'name')

@admin.register(RateHistory)
class RateHistoryAdmin(admin.ModelAdmin):
    list_display = ('currency', 'rate', 'timestamp')
    list_filter = ('currency', 'timestamp')