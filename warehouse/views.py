from django.shortcuts import render
from rest_framework import viewsets

from warehouse.models import WarehouseItem
from warehouse.serializers import WarehouseItemSerializer


class WarehouseItemViewSet(viewsets.ModelViewSet):
    queryset = WarehouseItem.objects.all()
    serializer_class = WarehouseItemSerializer
