from django.db import models

# Create your models here.
class Registration(models.Model):
        name=models.CharField(max_length=255)
        username=models.CharField(max_length=255)
        email=models.CharField(max_length=255)
        mobno=models.CharField(max_length=255)
        password=models.CharField(max_length=255)   
        conpassword=models.CharField(max_length=255)   

class Meta:
        db_table="LoginForm"