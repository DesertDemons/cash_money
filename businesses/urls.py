from django.urls import path
from businesses import views

urlpatterns = [
path('home/', views.home, name="home"),
]