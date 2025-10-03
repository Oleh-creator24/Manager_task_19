from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views_tasks import (
    TaskListCreateGenericView,
    TaskRetrieveUpdateDestroyGenericView,
    TaskListByDayView,
)
from .views_subtasks import (
    SubTaskListCreateGenericView,
    SubTaskRetrieveUpdateDestroyGenericView,
)
from .views_categories import CategoryViewSet
from . import views  # для task_list_html и api_task_stats

# --- Роутер для CategoryViewSet ---
router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    # HTML (оставляем для теста)
    path("", views.task_list_html, name="home"),

    # --- JWT Auth ---
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # --- Tasks (Generic Views) ---
    path("api/tasks/", TaskListCreateGenericView.as_view(), name="task-list-create"),
    path("api/tasks/<int:pk>/", TaskRetrieveUpdateDestroyGenericView.as_view(),
         name="task-detail-update-delete"),
    path("api/tasks-by-day/", TaskListByDayView.as_view(), name="tasks_by_day"),

    # --- SubTasks (Generic Views) ---
    path("api/subtasks/", SubTaskListCreateGenericView.as_view(), name="subtask-list-create"),
    path("api/subtasks/<int:pk>/", SubTaskRetrieveUpdateDestroyGenericView.as_view(),
         name="subtask-detail-update-delete"),

    # --- Статистика (FBV) ---
    path("api/stats/", views.api_task_stats, name="api_task_stats"),

    # --- Categories (ViewSet) ---
    path("api/", include(router.urls)),
]
