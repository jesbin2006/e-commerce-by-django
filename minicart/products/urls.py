from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index ,name='home'),
    path('products/',views.products,name='products'),
    path('product_details/<pk>',views.detail_product,name='detail_product')
]
