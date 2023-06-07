from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:pk>/', views.viewpost, name='post'),
    path('add/', views.addpost, name='add'),
    
    path('about/', views.aboutus, name='about'),
    path('contact/', views.contact, name='contact'),
    path('journal/', views.journalview.as_view(), name='journal'),
]