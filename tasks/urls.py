# tasks/urls.py
from django.urls import path
from .views import register_view, login_view, logout_view, task_list_view, task_detail_view, task_create_view, task_update_view, task_delete_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', task_list_view, name='task_list'),
    path('task/<int:pk>/', task_detail_view, name='task_detail'),
    path('task/new/', task_create_view, name='task_create'),
    path('task/<int:pk>/edit/', task_update_view, name='task_update'),
    path('task/<int:pk>/delete/', task_delete_view, name='task_delete'),
]
