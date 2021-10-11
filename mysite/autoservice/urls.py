from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name="cars"),
    path('car/<int:car_id>', views.car, name='car'),
    path('order/', views.OrderListView.as_view(), name='orders'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('search/', views.search, name='search'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('user_order/', views.UserOrderListView.as_view(), name='user-orders'),
]