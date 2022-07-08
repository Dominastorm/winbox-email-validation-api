from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('mail/<str:email>', views.MailView.as_view(), name='mail'),
    path('validate/regex/<str:email>', views.RegexView.as_view(), name='regex'),
]
