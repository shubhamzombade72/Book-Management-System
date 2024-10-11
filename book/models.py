from django.db import models

# Create your models here.
class Books(models.Model):
    b_name= models.CharField(max_length=255)
    b_author=models.CharField(max_length=255)
    b_prize=models.CharField(max_length=255)
    b_category=models.CharField(max_length=255)

    class Meta:
     db_table= 'Book_table'
    