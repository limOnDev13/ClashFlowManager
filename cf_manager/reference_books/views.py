from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class StatusViewSet(ModelViewSet):
    """ViewSet for Status."""

    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer


class TypeViewSet(ModelViewSet):
    """ViewSet for Type."""

    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer


class CategoryViewSet(ModelViewSet):
    """ViewSet for Category."""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class SubcategoryViewSet(ModelViewSet):
    """ViewSet for Subcategory."""

    queryset = models.Subcategory.objects.all()
    serializer_class = serializers.SubcategorySerializer

    def get_queryset(self):
        """Return subcategories by category_id, if category_id is query params."""
        queryset = super().get_queryset()
        category_id = self.request.query_params.get("category_id")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset
