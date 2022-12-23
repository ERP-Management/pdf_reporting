from django.contrib import admin
from .models import Student,Customers

# Register your models here.
@admin.register(Student)
class StudentAmdin(admin.ModelAdmin):
    list_display=['id','name','roll_no']

@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','cust_name','father_name']
