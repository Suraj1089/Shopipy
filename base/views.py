from django.shortcuts import render
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
def home(request):
    return render(request,'home.html')

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request,'registraion Successfully')
                return redirect('login')

    return render(request,'base/signup.html')

def login_user(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.info(request,'Username or Password is incorrect')
    return render(request,'base/signin.html')


def product_detailed_view(request):
    return render(request,'base/product_detailed_view.html')

def logout_user(request):
    return render(request,'base/login.html')

def render_chatbot(request):
    return render(request,'base/chatbot.html')