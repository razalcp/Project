from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('this is doctor module')

def index(request):
    return render(request,'doctor_templates/home.html')


def login(request):
    return render(request,'doctor_templates/login.html')    

def signup(request):
    return render(request,'doctor_templates/sign_up.html')      

