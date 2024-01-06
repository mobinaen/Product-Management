from django.urls import path
from . import views


urlpatterns = [
    path("customUser/create", views.CustomUserView.create),
    path("customUser/index", views.CustomUserView.index),
    path("customUser/update", views.CustomUserView.update),
    path("customUser/delete", views.CustomUserView.delete),
]