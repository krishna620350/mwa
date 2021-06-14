# shop url file
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('track/', views.track, name='track'),
    path('service/', views.service, name='service'),
    path('productview/', views.productview, name='productview'),
    path('product/', views.product, name='product'),
    path('search/', views.search, name='search'),
]
