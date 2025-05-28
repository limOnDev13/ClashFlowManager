from reference_books import models
from rest_framework import serializers


class StatusSerializer(serializers.ModelSerializer):
    """Cash flow status serializer."""

    class Meta:
        model = models.Status
        fields = ("id", "name")
        read_only_fields = ("id",)
