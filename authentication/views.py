from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from .models import User


# Create your views here.
def index(request):
    return HttpResponse("<h1> Hello jwt </h1>")


class RegistrationAPIView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    def post(self, request, *args):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer
    # renderer_classes = (UserJSONRenderer, )
    queryset = User.objects.all()

    def post(self, request, *args):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)