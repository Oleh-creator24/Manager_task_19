
from django.urls import path
from .views_tasks import (
    TaskListCreateGenericView,
    TaskRetrieveUpdateDestroyGenericView,
    TaskListByDayView,
)
from .views_subtasks import (
    SubTaskListCreateGenericView,
    SubTaskRetrieveUpdateDestroyGenericView,
)
from . import views  # только для task_list_html и api_task_stats

urlpatterns = [
    # HTML (оставим для теста)
    path("", views.task_list_html, name="home"),

    # --- Tasks (Generic Views) ---
    path("api/tasks/", TaskListCreateGenericView.as_view(), name="task-list-create"),
    path("api/tasks/<int:pk>/", TaskRetrieveUpdateDestroyGenericView.as_view(),
         name="task-detail-update-delete"),
    path("api/tasks-by-day/", TaskListByDayView.as_view(), name="tasks_by_day"),

    # --- SubTasks (Generic Views) ---
    path("api/subtasks/", SubTaskListCreateGenericView.as_view(), name="subtask-list-create"),
    path("api/subtasks/<int:pk>/", SubTaskRetrieveUpdateDestroyGenericView.as_view(),
         name="subtask-detail-update-delete"),

    # --- Статистика (оставляем FBV) ---
    path("api/stats/", views.api_task_stats, name="api_task_stats"),
]
