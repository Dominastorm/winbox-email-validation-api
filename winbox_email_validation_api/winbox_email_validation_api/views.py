from backend.tests.email_regex import email_regex_check
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class MailView(APIView):
    def get(self, request, email):
        return Response({'email': email})

class RegexView(APIView):
    def get(self, request, email):
        return Response({
            'test': 'regex',
            'email': email,
            'result': ['invalid', 'valid'][email_regex_check(email)]
        })
