from rest_framework import serializers

from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):  # type: ignore[type-arg]
    class Meta:
        model = Animal
        fields = ["id", "name", "age", "type", "sound", "color"]


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password_again = serializers.CharField()
