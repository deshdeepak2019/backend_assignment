from rest_framework import serializers

from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):  # type: ignore[type-arg]
    class Meta:
        model = Animal
        fields = ["id", "name", "age", "type", "sound", "color"]
