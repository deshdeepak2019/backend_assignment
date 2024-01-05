from typing import Any

from django.db.models.query import QuerySet
from django.utils import timezone
from rest_framework import mixins, status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from core.models import Animal
from core.serializers import AnimalSerializer


class AnimalViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,  # type:ignore[type-arg]
):
    """API view set for Elevator model."""

    queryset = Animal.objects.filter(deleted_on=None)
    serializer_class = AnimalSerializer

    def get_queryset(self) -> QuerySet[Animal]:
        return super().get_queryset()

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = AnimalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super().create(request, *args, **kwargs)

    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        try:
            animal = Animal.objects.get(pk=kwargs["pk"])
        except Animal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        animal.deleted_on = timezone.now()
        animal.save(update_fields=["deleted_on"])
        return Response(status=status.HTTP_204_NO_CONTENT)