from django.shortcuts import render

def home(request):
    return render(request,'to_do/home.html')