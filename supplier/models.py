from django.db import models

# Create your models here.
class Supplier(models.Model):
    S_Name=models.CharField( max_length=255)
    s_mobno=models.CharField(max_length=255)
    s_email=models.CharField(max_length=255)
    s_address=models.CharField(max_length=255)
    s_city=models.CharField(max_length=255)

class Meta:
    db_table='supplier'
