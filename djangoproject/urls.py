from django.contrib import admin
from django.urls import path
from test_app.views import greetings, TaskListCreateView, TaskRetrieveUpdateDestroyView, TaskStatsView, SubTaskListCreateView, SubTaskRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', greetings),
    path('api/tasks/', TaskListCreateView.as_view()),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view()),
    path('api/tasks/stats/', TaskStatsView.as_view()),
    path('api/subtasks/', SubTaskListCreateView.as_view()),
    path('api/subtasks/<int:pk>/', SubTaskRetrieveUpdateDestroyView.as_view()),
]
