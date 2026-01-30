from django.db import models
from tenant.models import CompanyBaseModel


class Expense(CompanyBaseModel):
    CATEGORY_CHOICES = [
        ('FOOD', 'Food'),
        ('TRANSPORT', 'Transport'),
        ('OFFICE', 'Office'),
        ('OTHER', 'Other'),
    ]

    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='OTHER'
    )
    expense_date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.amount})"

    class Meta:
        permissions = [
            ("view_all_expenses", "Can view all company expenses"),
        ]
