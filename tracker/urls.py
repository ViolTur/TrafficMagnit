from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyViewSet, RateHistoryViewSet

# Створюємо роутер
router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet)
router.register(r'history', RateHistoryViewSet)

# Експортуємо лише локальні urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]