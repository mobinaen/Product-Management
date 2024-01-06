from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from .models import Category, CustomUser, Product, Customer, OrderItem
from .serializers import ProductSerializer, CategorySerializer, CustomUserSerializer, CustomerSerializer, OrderItemSerializer


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


class CategoryView:
    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.AllowAny,))
    def create(request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.AllowAny,))
    def index(request):
        name = request.GET["name"]
        category = Category.objects.get(name=name)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class ProductView:
    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.AllowAny,))
    def create(request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.AllowAny,))
    def index(request):
        name = request.GET["name"]
        product = Product.objects.get(name=name)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    @staticmethod
    @api_view(['PATCH'])
    @permission_classes((permissions.AllowAny,))
    def update(request):
        name = request.GET["name"]
        Product.objects.filter(name=name).update(**request.data)
        serializer = ProductSerializer(Product.objects.get(name=name))
        return Response(serializer.data)

    @staticmethod
    @api_view(['DELETE'])
    @permission_classes((permissions.AllowAny,))
    def delete(request):
        name = request.GET["name"]
        Product.objects.filter(name=name).delete()
        return Response("OK")

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.AllowAny,))
    def moreThan10000(request):
        items = Product.objects.filter(price__gte=10000).all()
        serializer = ProductSerializer(items, many=True)
        return Response(serializer.data)

class CustomerView:
    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.AllowAny,))
    def index(request):
        name = request.GET["name"]
        item = Customer.objects.all()
        serializer = CustomerSerializer(item[0])
        return Response(serializer.data)


class OrderItemView:
    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.AllowAny,))
    def create(request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.AllowAny,))
    def index(request):
        id = request.GET["id"]
        item = OrderItem.objects.get(id=id)
        serializer = OrderItemSerializer(item)
        return Response(serializer.data)

    @staticmethod
    @api_view(['PATCH'])
    @permission_classes((permissions.AllowAny,))
    def update(request):
        id = request.GET["id"]
        OrderItem.objects.filter(id=id).update(**request.data)
        serializer = OrderItemSerializer(OrderItem.objects.get(id=id))
        return Response(serializer.data)

    @staticmethod
    @api_view(['DELETE'])
    @permission_classes((permissions.AllowAny,))
    def delete(request):
        id = request.GET["id"]
        OrderItem.objects.filter(id=id).delete()
        return Response("OK")

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.AllowAny,))
    def completed(request):
        items = OrderItem.objects.filter(is_completed__exact=True).all()
        serializer = OrderItemSerializer(items, many=True)
        return Response(serializer.data)