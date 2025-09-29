from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskDetailSerializer

class TaskListByDayView(APIView):
    def get(self, request):
        day = request.query_params.get("day")
        tasks = Task.objects.all()

        if day:
            tasks = tasks.filter(deadline__week_day=self._day_to_number(day))

        serializer = TaskDetailSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def _day_to_number(self, day: str):
        days = {
            "sunday": 1, "monday": 2, "tuesday": 3,
            "wednesday": 4, "thursday": 5, "friday": 6, "saturday": 7
        }
        return days.get(day.lower())
