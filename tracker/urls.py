from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyViewSet, RateHistoryViewSet

router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet)
router.register(r'history', RateHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]