from datetime import date

from cash_flows.models import CashFlow
from reference_books.models import Category, Status, Subcategory, Type
from rest_framework import serializers


class ClashFlowSerializer(serializers.ModelSerializer):
    """Cash flow serializer."""

    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
    type = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.select_related("type").all()
    )
    subcategory = serializers.PrimaryKeyRelatedField(
        queryset=Subcategory.objects.select_related("category").all()
    )

    class Meta:
        model = CashFlow
        fields = (
            "id",
            "creation_date",
            "status",
            "type",
            "category",
            "subcategory",
            "amount",
            "comment",
        )
        read_only_fields = ("id",)

    def validate_creation_date(self, value: date):
        if value is None or value > date.today():
            return date.today()
        return value

    def validate(self, data):
        """Check that the subcategory refers to the category, the category to the type."""
        subcategory, category, type_ = (
            data["subcategory"],
            data["category"],
            data["type"],
        )
        if subcategory.category.pk != category.pk:
            raise serializers.ValidationError(
                "A subcategory is not related to a category."
            )
        if category.type.pk != type_.pk:
            raise serializers.ValidationError(
                "A category is not related to a type."
            )

        return data
