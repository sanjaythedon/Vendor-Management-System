from django.urls import path
from vendors import views

app_name = 'vendors'

urlpatterns = [
    path('', views.vendors, name='vendor'),
]
