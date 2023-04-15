from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('<int:todo_id>/delete_todo/', views.delete_todo, name='delete_todo'),
    path('<int:todo_id>/edit_todo/', views.edit_todo, name='edit_todo'),
    path('delete_all_todo/', views.delete_all_todo, name='delete_all_todo'),
    path('toggle_status_todo/', views.toggle_status_todo, name='toggle_status_todo'),
]