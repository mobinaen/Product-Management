from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from .models import Product, CustomUser
from .serializers import ProductSerializer, CustomerSerializer, CustomUserSerializer


class CustomUserView:
    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.AllowAny,))
    def create(request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.AllowAny,))
    def index(request):
        username = request.GET["username"]
        customUsers = CustomUser.objects.get(username=username)
        serializer = CustomUserSerializer(customUsers)
        return Response(serializer.data)

    @staticmethod
    @api_view(['PATCH'])
    @permission_classes((permissions.AllowAny,))
    def update(request):
        username = request.GET["username"]
        CustomUser.objects.filter(username=username).update(**request.data)
        serializer = CustomUserSerializer(CustomUser.objects.get(username=username))
        return Response(serializer.data)

    @staticmethod
    @api_view(['DELETE'])
    @permission_classes((permissions.AllowAny,))
    def delete(request):
        username = request.GET["username"]
        CustomUser.objects.filter(username=username).delete()
        return Response("OK")
