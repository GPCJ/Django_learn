# blog/urls.py
from django.urls import path
from . import views

# FBV방식
urlpatterns = {
    # blog뒤에 int값이 있있으면 views파일 안에 single_post_page함수 실행
    path('<int:pk>/', views.single_post_page),
    # blog뒤에 아무것도 없으면 views파일 안에 index함수 실행
    path('', views.index),
}