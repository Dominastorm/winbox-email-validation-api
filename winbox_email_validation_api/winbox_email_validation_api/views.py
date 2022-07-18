from rest_framework.views import APIView
from rest_framework.response import Response
from backend.tests.catch_all import catch_all_test
from backend.tests.disposable_email import disposable_email_check
from backend.tests.email_regex import email_international_regex_check, email_regex_check
from backend.tests.free_email import free_email_check
from backend.tests.mx import mx_test
from backend.tests.role_account import role_account_check
from backend.tests.smtp import smtp_test
from backend.tests.temporary_unavalability import temporary_unavailability_check
from backend.tests.yahoo_test import yahoo_test


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


class InternationalRegexView(APIView):
    def get(self, request, email):
        return Response({
            'test': 'international regex',
            'email': email,
            'result': ['invalid', 'valid'][email_international_regex_check(email)]
        })


class MXView(APIView):
    def get(self, request, email):
        return Response({
            'test': 'mx',
            'email': email,
            'result': ['invalid', 'valid'][mx_test(email)]
        })


class SMTPView(APIView):
    def get(self, request, email):
        return Response({
            'test': 'smtp',
            'email': email,
            'result': ['invalid', 'valid'][smtp_test(email)]
        })


class YahooView(APIView):
    def get(self, request, email):
        return Response({
            'test': 'yahoo',
            'email': email,
            'result': ['invalid', 'valid', 'Not a Yahoo Email'][yahoo_test(email)]
        })


class DisposableEmailView(APIView):
    def get(self, request, email):
        return Response({
            'test': 'disposable email',
            'email': email,
            'result': ['no', 'yes'][disposable_email_check(email)]
        })


class RoleAccountView(APIView):
    def get(self, request, email):
        return Response({
            'test': 'role account',
            'email': email,
            'result': ['no', 'yes'][role_account_check(email)]
        })


class CatchAllView(APIView):
    def get(self, request, email):
        return Response({
            'test': 'catch all',
            'email': email,
            'result': ['no', 'yes'][catch_all_test(email)]
        })


class FreeEmailView(APIView):
    def get(self, request, email):
        return Response({
            'test': 'free email',
            'email': email,
            'result': ['no', 'yes'][free_email_check(email)]
        })


class TemporaryUnavailabilityView(APIView):
    def get(self, request, email):
        return Response({
            'test': 'temporary unavailability',
            'email': email,
            'result': temporary_unavailability_check(email)
        })
