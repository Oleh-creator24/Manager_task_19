from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/token/", include("rest_framework_simplejwt.urls")),  # если ты JWT подключал
    path("", include("tasks.urls")),  # ✅ подключаем роуты из tasks
]
