from rest_framework import viewsets
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        qs = Expense.objects.all()
        user = self.request.user
        if user.is_superuser:
            return qs
        if user.role == 'ADMIN':
            return qs.filter(company__owner=user)
        return qs.filter(company__owner=user, created_by=user)

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.owned_companies.first(), created_by=self.request.user)
