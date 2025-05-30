from cash_flows import models
from django import forms
from reference_books.models import Category


class CashFlowForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label="Category",
        help_text="Depending on the category, "
        "you will be offered a choice of appropriate subcategories. "
        "If no category is selected, all subcategories will be offered.",
    )

    class Meta:
        model = models.CashFlow
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # для редактирования существующей записи ClashFlow
        if self.instance and self.instance.subcategory:
            self.fields["category"].initial = (
                self.instance.subcategory.category
            )
