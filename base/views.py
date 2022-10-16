from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def register_user(request):
    return render(request,'base/signup.html')

def login_user(request):
    return render(request,'base/signin.html')


def product_detailed_view(request):
    return render(request,'base/product_detailed_view.html')

