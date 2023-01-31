from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/orders/', views.orders, name='orders'),
    path('dashboard/orders/pending', views.orders, name='orders-pending'),
    path('dashboard/orders/new', views.orders, name='orders-new'),
    path('dashboard/orders/update', views.updateorders, name='orders-update'),
    ]