from django.urls import path
from profile_grades import views


urlpatterns = [
    path('profilelikes/', views.ProfileLikeList.as_view()),
    path('profilelikes/<int:pk>/', views.ProfileLikeDetail.as_view()),
]