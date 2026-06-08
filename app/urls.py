from django.urls import path
from .views import task_list, task_details, add_task, edit_task, delete_task, login_view, register_view, logout_view
urlpatterns = [
    path('', task_list, name='task_list'),
    path('task_details/<int:id>/', task_details, name='task_details'),
    path('add_task/', add_task, name='add_task'),
    path('edit_task/<int:id>/', edit_task, name='edit_task'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    ]

