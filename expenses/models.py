from django.db import models
from tenant.models import CompanyBaseModel

class Expense(CompanyBaseModel):
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    expense_date = models.DateField()

    class Meta:
        permissions = [
            ("view_all_expenses", "Can view all company expenses"),
        ]

    def __str__(self):
        return f"{self.title} - {self.amount}"
