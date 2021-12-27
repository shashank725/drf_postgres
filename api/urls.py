from django.urls import path
from . import views

urlpatterns = [
    path('task/new/', views.taskNew, name="task-new"),
    path('task/all/',views.taskAll , name="task-all"),
]
