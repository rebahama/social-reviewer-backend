from django.contrib import admin
from django.urls import path
from profiles import views


urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileListDetail.as_view()),
]