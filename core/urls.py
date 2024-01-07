from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view  # type: ignore

from core.router import router

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
    path("", include(router.urls)),
]
