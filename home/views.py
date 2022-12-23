from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is my home page")

def  abount(req):
    return HttpResponse("this is my about page")

def new_method(req):
    return HttpResponse("this is my new method")
