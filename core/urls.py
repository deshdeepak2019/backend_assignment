from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from core import viewsets

router = DefaultRouter()
urlpatterns = [
    path(
        "openapi/",
        get_schema_view(
            title="Animal App",
            description="All API's for Animal App",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
    path(
        "",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]
router.register("elevator-system", viewsets.AnimalViewSet, basename="elevator-system")


urlpatterns += [
    path("", include(router.urls)),
]
