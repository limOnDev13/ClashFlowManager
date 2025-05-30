from rest_framework.viewsets import ModelViewSet

from . import models, serializers
from .signals.cache import cache_prefixes
from .utils.decorators.cache import cache_get_methods


@cache_get_methods(prefix=cache_prefixes.STATUSES_CACHE_PREFIX)
class StatusViewSet(ModelViewSet):
    """ViewSet for Status."""

    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer


@cache_get_methods(prefix=cache_prefixes.TYPES_CACHE_PREFIX)
class TypeViewSet(ModelViewSet):
    """ViewSet for Type."""

    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer


@cache_get_methods(prefix=cache_prefixes.CATEGORIES_CACHE_PREFIX)
class CategoryViewSet(ModelViewSet):
    """ViewSet for Category."""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


@cache_get_methods(prefix=cache_prefixes.SUBCATEGORIES_CACHE_PREFIX)
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
