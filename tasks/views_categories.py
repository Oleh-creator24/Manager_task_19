from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """CRUD для категорий + мягкое удаление + кастомный метод count_tasks"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=["get"])
    def count_tasks(self, request, pk=None):
        """Возвращает количество задач в категории"""
        category = self.get_object()
        count = category.tasks.count()  # ✅ связь через related_name
        return Response({"category": category.name, "tasks_count": count})
