from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:homework_id>/homework/', views.homework, name='homework'),
    path('<int:homework_id>/homework/answer/', views.AnswerHomework, name='answer'),
    path('<int:homework_id>/homework/review/', views.ReviewHomework, name='review'),
    path('statistics/', views.CountHomework, name='statistics'),
]