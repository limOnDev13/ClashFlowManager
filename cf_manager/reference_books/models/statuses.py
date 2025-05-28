from django.db import models


# Create your models here.
class Status(models.Model):
    """Cash flow status."""

    name: str = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True,
        help_text="Cash flow status name",
    )

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self) -> str:
        return self.name
