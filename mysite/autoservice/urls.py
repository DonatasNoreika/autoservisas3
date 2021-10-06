from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name="cars"),
    path('car/<int:car_id>', views.car, name='car'),
    path('books/', views.OrderListView.as_view(), name='orders'),
    path('books/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('search/', views.search, name='search'),
]