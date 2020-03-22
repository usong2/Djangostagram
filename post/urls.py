from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.detail),
    path('timeline/', views.timeline),
    path('upload/', views.upload),
]