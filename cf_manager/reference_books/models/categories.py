from django.db import models


class Category(models.Model):
    """Cash flow category model."""

    name: str = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True,
        help_text="Clash flow category name",
    )

    type: "Type" = models.ForeignKey(
        "Type",
        on_delete=models.CASCADE,
        related_name="categories",
        null=False,
        help_text="Parent type",
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "type"],
                name="unique_category_per_type",
            )
        ]

    def __str__(self) -> str:
        return self.name


class Subcategory(models.Model):
    """Cash flow subcategory model."""

    name: str = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        help_text="Clash flow subcategory name",
    )
    category: "Category" = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="subcategories",
        null=False,
        help_text="Parent category",
    )

    class Meta:
        verbose_name_plural = "Subcategories"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "category"],
                name="unique_subcategory_per_category",
            )
        ]

    def __str__(self) -> str:
        return self.name
