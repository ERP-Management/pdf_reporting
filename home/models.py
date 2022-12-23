from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll_no=models.CharField(max_length=100)

class Customers(models.Model):
    cust_name= models.CharField(max_length=1000)
    father_name=models.CharField(max_length=1000)