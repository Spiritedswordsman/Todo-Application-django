from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('task/create/', views.create_task, name='create-task'),
    path('task/edit/<int:task_id>/', views.edit_task, name='edit-task'),
    path('task/delete/<int:task_id>/', views.delete_task, name='delete-task'),
    path('task/filter/', views.filter_tasks, name='filter-tasks'),
]
