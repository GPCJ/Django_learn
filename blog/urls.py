from django.urls import path
from . import views

# FBV방식
urlpatterns = {
    path('', views.index),
}