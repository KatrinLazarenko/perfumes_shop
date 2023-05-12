from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

from .permissions import IsAdmin
from .serializers import CustomerSerializer, ManagerSerializer, AdminSerializer


User = get_user_model()


class CustomerCreateView(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]


class ManagerCreateView(generics.CreateAPIView):
    serializer_class = ManagerSerializer
    permission_classes = [IsAdmin]


class AdminCreateView(generics.CreateAPIView):
    serializer_class = AdminSerializer
    permission_classes = [IsAdmin]
