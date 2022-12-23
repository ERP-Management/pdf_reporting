from django.shortcuts import render,HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
import pandas as pd
# from django.conf.urls import url



# Create your views here.
def index(request):
    return HttpResponse("this is my home page")

def abount(req):
    print('now server in about page method')
    return HttpResponse("this is my about page")

def student_detail(req,pk):
    stud= Student.objects.get(id=pk)
    sr= StudentSerializer(stud)
    print("all student list is")
    print(stud)
    json_data=JSONRenderer().render(sr.data)
    return HttpResponse(json_data,content_type="application/json")

def student_get_all(req):
    studs= Student.objects.all()

    for std in studs:
        print('studetnt name is ')
        print(std.name)
        print ('student roll number is')
        print(std.roll_no)
    
    sr= StudentSerializer(studs,many=True)
    print("all student list is")
    print(studs)
    json_data=JSONRenderer().render(sr.data)
    return HttpResponse(json_data,content_type="application/json")

def  abount(req):
    print("this is my about page")
    return HttpResponse("this is my about page")

def new_method(req):
    return HttpResponse("this is my new method")
