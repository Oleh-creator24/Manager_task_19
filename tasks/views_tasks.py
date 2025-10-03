# tasks/views_tasks.py
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskCreateSerializer, TaskDetailSerializer


# --- Список и создание задач ---
class TaskListCreateGenericView(generics.ListCreateAPIView):
    """
    GET /api/tasks/?status__name=Done&ordering=-created_at
    POST /api/tasks/
    """
    queryset = Task.objects.all().order_by("-deadline")
    serializer_class = TaskCreateSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = {
        "status": ["exact"],
        "status__name": ["iexact"],
        "deadline": ["gte", "lte"],
    }
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "deadline"]   # ✅ исправлено (created убрал)


# --- Деталь, обновление и удаление задачи ---
class TaskRetrieveUpdateDestroyGenericView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/tasks/<pk>/
    PATCH /api/tasks/<pk>/
    PUT /api/tasks/<pk>/
    DELETE /api/tasks/<pk>/
    """
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


# --- Список задач по дню недели ---
class TaskListByDayView(generics.ListAPIView):
    """
    GET /api/tasks-by-day/?day=Monday
    """
    serializer_class = TaskDetailSerializer

    def get_queryset(self):
        tasks = Task.objects.all()
        day = self.request.query_params.get("day")

        if day:
            weekday_map = {
                "sunday": 1,
                "monday": 2,
                "tuesday": 3,
                "wednesday": 4,
                "thursday": 5,
                "friday": 6,
                "saturday": 7,
            }
            day_num = weekday_map.get(day.lower())
            if day_num:
                tasks = tasks.filter(deadline__week_day=day_num)
        return tasks.order_by("-deadline")
