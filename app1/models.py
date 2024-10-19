from django.db import models

# Create your models here.
class Logins(models.Model):
    usname=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    conpassword=models.CharField(max_length=255)

class Meta:
    db_table="logins"
