from django.urls import path

from .views import (
    CertificatesListApiView,
    DegreesListApiView,
    JobsListApiView,
    ProjectsListApiView,
    SkillsListApiView,
    GetAllApiView,
)

urlpatterns = [
    path("certificates", CertificatesListApiView.as_view()),
    path("degrees", DegreesListApiView.as_view()),
    path("jobs", JobsListApiView.as_view()),
    path("projects", ProjectsListApiView.as_view()),
    path("skills", SkillsListApiView.as_view()),
    path("get_all", GetAllApiView.as_view()),
]
