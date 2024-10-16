from django.contrib import admin
from loginForms.models import Registration
# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display=("name","username","email","mobno","password","conpassword",)
admin.site.register(Registration,RegistrationAdmin)