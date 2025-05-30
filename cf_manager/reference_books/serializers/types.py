from reference_books import models
from rest_framework import serializers


class TypeSerializer(serializers.ModelSerializer):
    """Cash flow type serializer."""

    class Meta:
        model = models.Type
        fields = ("id", "name")
        read_only_fields = ("id",)
