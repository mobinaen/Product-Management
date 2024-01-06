from django.urls import path
from . import views


urlpatterns = [
    path("customUser/create", views.CustomUserView.create),
    path("customUser/index", views.CustomUserView.index),
    path("customUser/update", views.CustomUserView.update),
    path("customUser/delete", views.CustomUserView.delete),

    path("category/create", views.CategoryView.create),
    path("category/index", views.CategoryView.index),

    path("product/create", views.ProductView.create),
    path("product/index", views.ProductView.index),
    path("product/update", views.ProductView.update),
    path("product/delete", views.ProductView.delete),

    # path("customer/index", views.CustomerView.index),

    path("orderItem/create", views.OrderItemView.create),
    path("orderItem/index", views.OrderItemView.index),
    path("orderItem/update", views.OrderItemView.update),
    path("orderItem/delete", views.OrderItemView.delete),
]