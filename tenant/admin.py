from django.contrib import admin
from tenant.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'is_active')
    search_fields = ('name',)
