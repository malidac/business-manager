from django.contrib import admin
from expenses.models import Expense
from tenant.permissions import is_company_admin


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'expense_date')
    list_filter = ('category',)
    search_fields = ('title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.role == 'ADMIN':
            return qs.filter(company=request.company)
        return qs.filter(company=request.company, created_by=request.user)

    def has_add_permission(self, request):
        return request.user.is_superuser or is_company_admin(request.user)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or is_company_admin(request.user)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or is_company_admin(request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.company = request.company
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
