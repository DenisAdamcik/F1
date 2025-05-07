from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('drivers/', views.DriverListView.as_view(), name='driver_list'),
    path('drivers/<int:pk>/', views.DriverDetailView.as_view(), name='driver_detail'),

    path('teams/', views.TeamListView.as_view(), name='team_list'),
    path('teams/<int:pk>/', views.TeamDetailView.as_view(), name='team_detail'),

    path('cars/', views.CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
]
