from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Prtoduct,Customer,Oreder
from .serializers import PrtoductSerializer, CustomerSerializer,OrederSerializer

# Create your views here.

@api_view(['POST'])
def add_Product(request):
    serializer = PrtoductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "New Product is added"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_Product(request):
    product = Prtoduct.objects.all()
    serializer = PrtoductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "New Customer is added"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_Oreder(request):
    serializer = OrederSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "New Oreder is added"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def order_details(request, order_id):
    order = get_object_or_404(Oreder, pk=order_id)
    serializer = OrederSerializer(order)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def Mark_order(request, order_id):
    order = get_object_or_404(Oreder, pk=order_id)
    serializer = OrederSerializer(order, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Order status updated successfully ✅"}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def order_customer(request):
    orders = Oreder.objects.select_related('customer').all()
    serializer = OrederSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



