import os

from django.conf import settings
from django.conf.urls import url
from django.http import JsonResponse
from django.core.wsgi import get_wsgi_application

settings.configure(
    DEBUG=True,
    SECRET_KEY='I_AM_A_DUMMY_KEY_CHANGE_ME',
    ROOT_URLCONF='app.wsgi',
    ALLOWED_HOSTS=['*'],
)


def index(request):
    response = {'data': 'A minimal Django server'}
    return JsonResponse(response)

urlpatterns = [
    url(r'^$', index),
]

application = get_wsgi_application()
