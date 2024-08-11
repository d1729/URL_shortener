from django.urls import path

from shortner import views

urlpatterns = [
    path('create-short-url', views.ShortenerView.as_view()),
    path('<str:shortcode>/', views.ShortenerView.as_view())
]