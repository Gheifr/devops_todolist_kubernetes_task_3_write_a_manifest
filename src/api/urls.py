from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("liveness/", views.LivenessCheck.as_view(), name="liveness"),
    path("readyness/", views.ReadynessCheck.as_view(), name="readyness"),
]

# app_name = "api"