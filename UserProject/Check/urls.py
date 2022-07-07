from Check import views
from django.shortcuts import render
from django.urls import path, re_path
from .views import TaskDetail, TaskList

urlpatterns = [
    path('', TaskList.as_view(), name="task"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task")
]
