from django.urls import path

from api import views

urlpatterns = [
    path('student/<str:username>/', views.StudentView.as_view()),
    path('student/', views.StudentView.as_view()),
]
