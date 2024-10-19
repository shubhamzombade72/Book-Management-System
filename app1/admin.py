from django.contrib import admin
from app1.models import Logins
# Register your models here.
class loginAdmin(admin.ModelAdmin):
    list_display=("usname","email","password","conpassword",)
admin.site.register(Logins, loginAdmin)


