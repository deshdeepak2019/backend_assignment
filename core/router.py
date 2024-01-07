from rest_framework.routers import DefaultRouter  # type: ignore

from core import viewsets

router = DefaultRouter()

router.register("accounts", viewsets.UserViewSet, basename="accounts")
router.register("animal", viewsets.AnimalViewSet, basename="animal")
