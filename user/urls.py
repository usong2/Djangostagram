from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout),
    path('login/', views.login),
    path('register/', views.register),
]