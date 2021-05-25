from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializer


# Create your views here.
def index(request):
    return HttpResponse("<h1> Hello jwt </h1>")


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        seializer = self.serializer_class(data=user)
        seializer.is_valid(raise_exception=True)
        seializer.save()

        return Response(seializer.data, status=status.HTTP_201_CREATED)