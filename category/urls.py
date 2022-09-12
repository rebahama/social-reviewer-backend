""" Creating urls for the view of category,
    passing and integer in the second path """
from django.urls import path
from category import views

urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>', views.CategoryDetail.as_view()),

]
