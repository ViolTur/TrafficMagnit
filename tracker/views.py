from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Currency, RateHistory
from .serializers import CurrencySerializer, RateHistorySerializer
from .filters import RateHistoryFilter
from drf_spectacular.utils import extend_schema, OpenApiExample

class CurrencyViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def get_queryset(self):
        queryset = Currency.objects.all()
        active_param = self.request.query_params.get('active')
        if active_param is not None:
            is_active = active_param.lower() == 'true'
            queryset = queryset.filter(is_active=is_active)
        return queryset

    @extend_schema(
        summary="Додати нову валюту",
        description="Створює нову валюту в базі для подальшого моніторингу.",
        request=CurrencySerializer,
        examples=[
            OpenApiExample(
                'Приклад створення JPY',
                value={
                    "code": "JPY",
                    "name": "Японська єна",
                    "iso_code": 392,
                    "is_active": True
                }
            )
        ]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Увімкнути/вимкнути моніторинг",
        request=None,
        responses={200: CurrencySerializer},
    )
    @action(detail=True, methods=['patch'])
    def toggle(self, request, pk=None):
        currency = self.get_object()
        currency.is_active = not currency.is_active
        currency.save()
        status_text = "Увімкнено" if currency.is_active else "Вимкнено"
        return Response({
            'status': f'Валюту {currency.code} {status_text}',
            'is_active': currency.is_active
        })

class RateHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RateHistory.objects.all()
    serializer_class = RateHistorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RateHistoryFilter