from rest_framework import serializers
from .models import Certificate, Degree, Job, Project, Skill


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["id", "title", "school", "description", "dateAcquired"]


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ["id", "title", "school", "description", "dateFrom", "dateTo"]


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            "id",
            "positionTitle",
            "companyTitle",
            "description",
            "dateFrom",
            "dateTo",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "isFeatured",
            "description",
            "githubURL",
            "runningAppURL",
            "technologies",
            "images",
        ]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "title", "technologies"]
