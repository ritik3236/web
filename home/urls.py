from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bsc/', views.home, name='bsc'),
    path('bsc/<int:num>/', views.home, name='bsc'),

]
