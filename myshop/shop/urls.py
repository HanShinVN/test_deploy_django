from django.urls import path
from . import views
from .views import add_product


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', add_product, name='add_product'),
]
