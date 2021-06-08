from django.conf.urls import url
from django.urls import path, include
# from .api import RegisterApi
from .views import *
urlpatterns = [
        path('register/', RegistrationAPIView.as_view(), name='register'),
        path('login/', LoginAPIView.as_view(), name='login'),
        path('users/', UserView.as_view(), name='user'),
        path('current_user/', CurrentUserView.as_view(), name='current_user')

]