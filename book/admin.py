from django.contrib import admin
from book.models import Books

# Register your models here.
class bookAdmin(admin.ModelAdmin):
    list_display=("b_name","b_author","b_prize","b_category",)
admin.site.register(Books, bookAdmin)
