from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
    path('', views.Orders.as_view(), name='orders'),
    path('<int:id>', views.Order.as_view(), name='a_order')
]