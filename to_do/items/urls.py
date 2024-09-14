from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('dashboard', views.list_todo_items, name='list'),
    path('new/', views.create_todo_item, name='new'),
    path('edit/<int:id>', views.update_todo_item, name='update'),
    path('delete/<int:id>', views.delete_todo_item, name='delete'),
]

