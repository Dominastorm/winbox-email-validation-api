from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# from api.serializers import EmailSerializer
# from api.models import Email

class MailView(APIView):
    def get(self, request):
        return Response({'message': 'Hello, World!'})
