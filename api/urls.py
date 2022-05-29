from django.urls import path

from .views import (
    GetAllApiView,
)

urlpatterns = [
    path("get_all", GetAllApiView.as_view()),
]
