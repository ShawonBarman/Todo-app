from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.addToDoItem, name="add"),
    path('completed/<todo_id>', views.completedToDo, name="completed"),
    path('deleteCompleted', views.deleteCompleted, name="deleteCompleted"),
    path('deleteAll', views.deleteAll, name="deleteAll")
]