from django.contrib import admin
from reference_books import models as book_models

from . import forms, models


class StatusFilter(admin.SimpleListFilter):
    title = "status"
    parameter_name = "status_name"

    def lookups(self, request, model_admin):
        return [
            (status.name, status.name)
            for status in book_models.Status.objects.all()
        ]

    def queryset(self, request, queryset):
        if value := self.value():
            return queryset.filter(status__name=value)
        return queryset


class TypeFilter(admin.SimpleListFilter):
    title = "type"
    parameter_name = "type_name"

    def lookups(self, request, model_admin):
        return [
            (type_.name, type_.name)
            for type_ in book_models.Type.objects.all()
        ]

    def queryset(self, request, queryset):
        if value := self.value():
            return queryset.filter(subcategory__category__type__name=value)
        return queryset


class CategoryFilter(admin.SimpleListFilter):
    title = "category"
    parameter_name = "category_name"

    def lookups(self, request, model_admin):
        return [
            (category.name, category.name)
            for category in book_models.Category.objects.all()
        ]

    def queryset(self, request, queryset):
        if value := self.value():
            return queryset.filter(subcategory__category__name=value)
        return queryset


class SubcategoryFilter(admin.SimpleListFilter):
    title = "subcategory"
    parameter_name = "subcategory_name"

    def lookups(self, request, model_admin):
        return [
            (subcategory.name, subcategory.name)
            for subcategory in book_models.Subcategory.objects.all()
        ]

    def queryset(self, request, queryset):
        if value := self.value():
            return queryset.filter(subcategory__name=value)
        return queryset


# Register your models here.
@admin.register(models.CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    form = forms.CashFlowForm
    list_display = (
        "pk",
        "creation_date",
        "status",
        "category",
        "subcategory",
        "amount",
        "type",
    )
    list_display_links = "pk", "creation_date"
    search_fields = (
        "creation_date",
        "status__name",
        "subcategory__category__type__name",
        "subcategory__category__name",
        "subcategory__name",
    )
    list_filter = (
        "creation_date",
        StatusFilter,
        TypeFilter,
        CategoryFilter,
        SubcategoryFilter,
    )
    ordering = ("creation_date",)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        category_field = fields.pop()  # категория идет последним полем
        subcategory_index = fields.index("subcategory")
        # ставим категорию перед подкатегорией
        fields.insert(subcategory_index, category_field)
        return fields

    def get_queryset(self, request):
        return models.CashFlow.objects.select_related("status").select_related(
            "subcategory__category__type"
        )

    def subcategory(self, obj: models.CashFlow) -> str:
        return obj.subcategory.name

    def category(self, obj: models.CashFlow) -> str:
        return obj.subcategory.category.name

    def type(self, obj: models.CashFlow) -> str:
        return obj.subcategory.category.type.name

    def status(self, obj: models.CashFlow) -> str:
        return obj.status.name
