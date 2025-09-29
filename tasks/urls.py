from django.urls import path
from . import views
from .views_subtasks import (
    SubTaskListCreateView,
    SubTaskDetailUpdateDeleteView,
    SubTaskListView,      # ✅ Задание 2 (пагинация)
    SubTaskFilterView     # ✅ Задание 3 (фильтрация)
)
from .views_tasks import TaskListByDayView  # ✅ Задание 1

urlpatterns = [
    # HTML
    path("", views.task_list_html, name="home"),

    # --- Tasks (FBV, пока не переписаны на DRF полностью) ---
    path("api/tasks/create/", views.api_create_task, name="api_task_create"),
    path("api/tasks/", views.api_task_list, name="api_task_list"),
    path("api/tasks/<int:task_id>/", views.api_task_detail, name="api_task_detail"),
    path("api/tasks/<int:task_id>/subtasks/", views.api_task_subtasks, name="api_task_subtasks"),
    path("api/stats/", views.api_task_stats, name="api_task_stats"),

    # --- SubTasks (CBV на DRF) ---
    path("api/subtasks/", SubTaskListCreateView.as_view(), name="subtask-list-create"),
    path("api/subtasks/<int:pk>/", SubTaskDetailUpdateDeleteView.as_view(), name="subtask-detail-update-delete"),
    path("api/subtasks/create/", views.api_create_subtask, name="api_subtask_create"),

    # --- Задание 1: задачи по дню недели ---
    path("api/tasks-by-day/", TaskListByDayView.as_view(), name="tasks_by_day"),

    # --- Задание 2: список подзадач с пагинацией ---
    path("api/subtasks/list/", SubTaskListView.as_view(), name="subtasks_list"),

    # --- Задание 3: фильтрация подзадач по названию главной задачи и статусу ---
    path("api/subtasks/filter/", SubTaskFilterView.as_view(), name="subtasks_filter"),
]
