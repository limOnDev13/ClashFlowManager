from datetime import date
from decimal import Decimal

from django.db import models
from reference_books.models import Status, Subcategory


class CashFlow(models.Model):
    creation_date: date = models.DateField(
        verbose_name="Creation date",
        null=True,
        help_text="The date when the cash flow record was created. "
        "If you do not specify a value or specify a date from the future, "
        "the current date will be set.",
    )
    status: Status = models.ForeignKey(
        Status, on_delete=models.CASCADE, null=False
    )
    subcategory: Subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, null=False
    )
    amount: Decimal = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        help_text="The amount of funds in rubles",
    )
    comment: str = models.TextField(
        null=True, blank=True, help_text="Comment on the entry in free form."
    )

    class Meta:
        ordering = ("creation_date",)
        verbose_name = "Cash Flow"
        verbose_name_plural = "Cash Flows"

    def save(self, *args, **kwargs):
        if self.creation_date is None or self.creation_date > date.today():
            self.creation_date = date.today()

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.pk} | {self.creation_date} | {self.amount} RUB"
