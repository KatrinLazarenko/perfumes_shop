from rest_framework import serializers
from .models import CustomUser, Customer, Manager, Admin


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email", "password",)
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class CustomerSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Customer
        fields = ("id", "user", "address", "phone_number",)

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = CustomUser.objects.create_user(**user_data)
        customer = Customer.objects.create(user=user, **validated_data)
        return customer


class ManagerSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Manager
        fields = ("id", "user", "department",)

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = CustomUser.objects.create_manager(**user_data)
        manager = Manager.objects.create(user=user, **validated_data)
        return manager


class AdminSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Admin
        fields = ("id", "user",)

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = CustomUser.objects.create_superuser(**user_data)
        admin = Admin.objects.create(user=user, **validated_data)
        return admin
