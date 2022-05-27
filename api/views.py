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


class CertificatesListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        List all the certificate items
        """
        certificates = Certificate.objects
        serializer = CertificateSerializer(certificates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DegreesListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        List all the degree items
        """
        degrees = Degree.objects
        serializer = DegreeSerializer(degrees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class JobsListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        List all the Job items
        """
        jobs = Job.objects
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectsListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        List all the Project items
        """
        projects = Project.objects
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SkillsListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        List all the Skill items
        """
        skills = Skill.objects
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetAllApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None, *args, **kwargs):
        """
        List all items
        """
        certificates = SkillSerializer(Certificate.objects, many=True)

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
