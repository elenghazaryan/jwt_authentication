from django.conf.urls import url
from django.urls import path, include
# from .api import RegisterApi
from .views import *
urlpatterns = [
        path('register', RegistrationAPIView.as_view()),
]