from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Certificate, Degree, Job, Project, Skill
from .serializers import (
    CertificateSerializer,
    DegreeSerializer,
    JobSerializer,
    ProjectSerializer,
    SkillSerializer,
)


class GetAllApiView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        """
        List all items
        """
        certificates = CertificateSerializer(Certificate.objects, many=True)

        degrees = DegreeSerializer(Degree.objects, many=True)

        jobs = JobSerializer(Job.objects, many=True)

        projects = ProjectSerializer(Project.objects, many=True)

        skills = SkillSerializer(Skill.objects, many=True)

        return Response(
            {
                "certificates": certificates.data,
                "degrees": degrees.data,
                "jobs": jobs.data,
                "projects": projects.data,
                "skills": skills.data,
            },
            status=status.HTTP_200_OK,
        )
