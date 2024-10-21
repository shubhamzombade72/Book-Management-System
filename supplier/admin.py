from django.contrib import admin
from supplier.models import Supplier
# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    list_display=("S_Name","s_mobno","s_email","s_address","s_city",)

admin.site.register(Supplier,SupplierAdmin)