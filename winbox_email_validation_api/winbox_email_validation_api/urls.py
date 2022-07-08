from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('mail/<str:email>', MailView.as_view(), name='mail'),
    path('validate/regex/<str:email>', RegexView.as_view(), name='regex'),
    path('validate/international-regex/<str:email>', InternationalRegexView.as_view(), name='international-regex'),
    path('validate/mx/<str:email>', MXView.as_view(), name='mx'),
    path('validate/smtp/<str:email>', SMTPView.as_view(), name='smtp'),
    path('validate/yahoo/<str:email>', YahooView.as_view(), name='yahoo'),
    path('validate/disposable-email/<str:email>', DisposableEmailView.as_view(), name='disposable-email'),
    path('validate/role-account/<str:email>', RoleAccountView.as_view(), name='role-account'),
    path('validate/catch-all/<str:email>', CatchAllView.as_view(), name='catch-all'),
    path('validate/free-email/<str:email>', FreeEmailView.as_view(), name='free-email'),
    path('validate/temporary-unavailablity/<str:email>', TemporaryUnavailabilityView.as_view(), name='temporary-unavailability'),
]
