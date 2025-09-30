
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from .models import SubTask
from .serializers import SubTaskCreateSerializer, SubTaskDetailSerializer


# --- Пагинация для SubTasks ---
class SubTaskPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 5
    page_size_query_param = None


# --- Список и создание подзадач ---
class SubTaskListCreateGenericView(generics.ListCreateAPIView):
    """
    GET /api/subtasks/?status__name=In%20Progress&task__title=Project%20A&ordering=-created_at
    POST /api/subtasks/
    """
    queryset = SubTask.objects.all().order_by("-created_at")
    serializer_class = SubTaskCreateSerializer
    pagination_class = SubTaskPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = {
        "status": ["exact"],
        "status__name": ["iexact"],
        "deadline": ["gte", "lte"],
        "task": ["exact"],
        "task__title": ["icontains"],
    }
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "deadline"]


# --- Деталь, обновление и удаление подзадачи ---
class SubTaskRetrieveUpdateDestroyGenericView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/subtasks/<pk>/
    PATCH /api/subtasks/<pk>/
    PUT /api/subtasks/<pk>/
    DELETE /api/subtasks/<pk>/
    """
    queryset = SubTask.objects.all()
    serializer_class = SubTaskDetailSerializer
