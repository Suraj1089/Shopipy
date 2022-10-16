from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('product_detailed_view/', views.product_detailed_view, name='product_detailed_view'),
    path('login/', views.login_user, name='login'),
   

]

