from datetime import date
from decimal import Decimal

from django.db import models

from reference_books.models import Status, Subcategory


class CashFlow(models.Model):
    creation_date: date = models.DateField(
        verbose_name="Creation date",
        auto_now_add=True,
        null=False,
        blank=False,
        help_text="The date when the cash flow record was created."
    )
    status: Status = models.ForeignKey(Status, on_delete=models.CASCADE, null=False)
    subcategory: Subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=False)
    amount: Decimal = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        help_text="The amount of funds in rubles"
    )
    comment: str = models.TextField(null=True, blank=True, help_text="Comment on the entry in free form.")

    class Meta:
        ordering = ("creation_date",)
        verbose_name = "Cash Flow"
        verbose_name_plural = "Cash Flows"
