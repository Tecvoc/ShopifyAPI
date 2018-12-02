from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path('products', views.render_products),
    re_path('order', views.order_product, name="order"),

]