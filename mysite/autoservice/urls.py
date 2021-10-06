from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.authors, name="cars"),
    path('car/<int:car_id>', views.author, name='car'),
]