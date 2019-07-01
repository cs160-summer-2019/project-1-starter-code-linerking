from django.urls import path

from . import views

urlpatterns = [
    path('map/', views.map, name='map'),
    path('list/', views.list, name='list'),
    path('search/', views.search, name='search'),
    path('alert/', views.alert, name='comparison_alert'),
    path('', views.index, name='index'),
]