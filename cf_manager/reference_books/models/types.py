from django.db import models


# Create your models here.
class Type(models.Model):
    """Cash flow type."""

    name: str = models.CharField(
        max_length=30, null=False, blank=False, help_text="Cash flow type name"
    )

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self) -> str:
        return self.name
