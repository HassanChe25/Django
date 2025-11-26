from django.urls import path
from . import views

urlpatterns = [
    path('tp/add', views.add_customer, name='add_customer'),
    path('tp/add/order', views.add_Oreder, name='add_order'),
    path('tp/add/product', views.add_Product, name='add_product'),
    path('tp/all', views.get_all_Product, name='get_all_product'),
    path('tp/order/<int:order_id>', views.order_details, name='order_details'),
    path('tp/orders/customers', views.order_customer, name='order_customer'),
    path('tp/mark/order/<int:order_id>', views.Mark_order, name='mark_order'),
]

