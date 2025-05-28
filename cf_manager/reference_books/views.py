from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class StatusViewSet(ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer


class TypeViewSet(ModelViewSet):
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class SubcategoryViewSet(ModelViewSet):
    queryset = models.Subcategory.objects.all()
    serializer_class = serializers.SubcategorySerializer
