from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

# Register your models here.
from .models import Certificate, Degree, Job, Project, Skill


class CertificateAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "school", "description", "dateAcquired"]
    list_display_links = ["id"]
    list_editable = ["title", "school", "description", "dateAcquired"]


class DegreesAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "school", "dateFrom", "dateTo"]
    list_display_links = ["id"]
    list_editable = ["title", "school", "dateFrom", "dateTo"]


class JobsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "positionTitle",
        "companyTitle",
        "description",
        "dateFrom",
        "dateTo",
    ]
    list_display_links = ["id"]
    list_editable = [
        "positionTitle",
        "companyTitle",
        "description",
        "dateFrom",
        "dateTo",
    ]


class ProjectsAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = [
        "id",
        "title",
        "isFeatured",
        "description",
        "githubURL",
        "runningAppURL",
        "technologies",
        "images",
    ]
    list_display_links = ["id"]
    list_editable = [
        "title",
        "isFeatured",
        "description",
        "githubURL",
        "runningAppURL",
        "technologies",
        "images",
    ]


class SkillsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "technologies"]
    list_display_links = ["id"]
    list_editable = ["title", "technologies"]


admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Degree, DegreesAdmin)
admin.site.register(Job, JobsAdmin)
admin.site.register(Project, ProjectsAdmin)
admin.site.register(Skill, SkillsAdmin)
