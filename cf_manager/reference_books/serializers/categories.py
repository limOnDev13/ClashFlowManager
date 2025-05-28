from reference_books import models
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """Cash flow category serializer."""

    class Meta:
        model = models.Category
        fields = ("id", "name")
        read_only_fields = ("id",)


class SubcategorySerializer(serializers.ModelSerializer):
    """Cash flow subcategory serializer."""

    category = serializers.PrimaryKeyRelatedField(
        queryset=models.Category.objects.all()
    )

    class Meta:
        model = models.Status
        fields = ("id", "name", "category")
        read_only_fields = ("id",)
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=models.Subcategory.objects.all(),
                fields=("name", "category"),
                message="The category already has a subcategory with that name.",
            )
        ]
