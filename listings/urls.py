from django.urls import path, re_path
from . import views

# app_name = 'listings'

urlpatterns = [
    path('', views.listings, name='listings'),
    path('<int:pk>/', views.listing, name='listing'),
    path('search/', views.search, name='search'),
]