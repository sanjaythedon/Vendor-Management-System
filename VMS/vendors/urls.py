from django.urls import path
from vendors import views

app_name = 'vendors'

urlpatterns = [
    path('', views.VendorsList.as_view(), name='vendorList'),
    path('<int:id>', views.VendorsDetail.as_view(), name='vendorDetail')
]
