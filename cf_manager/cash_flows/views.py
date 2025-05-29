from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class CashFlowViewSet(ModelViewSet):
    """ViewSet for CashFlow."""

    queryset = (
        models.CashFlow.objects.select_related("subcategory__category__type")
        .select_related("status")
        .all()
    )
    serializer_class = serializers.ClashFlowSerializer
