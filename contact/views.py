from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from contact.serializers import EmailSerializer

from dotenv import load_dotenv
import os

load_dotenv()


class EmailApiView(APIView):
    def post(self, request, *args, **kwargs):
        """
        Send email from contact
        """
        data = {
            "name": request.data.get("name"),
            "email": request.data.get("email"),
            "message": request.data.get("message"),
        }

        serializer = EmailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            send_mail(
                subject=data.get("name"),
                message=data.get("message"),
                from_email=os.getenv("HOST_EMAIL"),
                recipient_list=[data.get("email")],
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
