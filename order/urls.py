from django.urls import path
from . import views
app_name="order"

urlpatterns = [
path('checkout/', views.checkout, name='checkout'),
path('orders/', views.my_orders, name='my_orders'),
path("order-detail/<int:order_id>/", views.order_detail, name="order_detail"),
path("order-success/<int:order_id>/", views.order_success, name="order_success"),
]