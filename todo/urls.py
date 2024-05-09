from django.urls import path

from todo.views import AddTask, TasksView


urlpatterns = [
    path('', TasksView.as_view(), name='tasks'),
    path('add/', AddTask.as_view(), name='add'),
]
