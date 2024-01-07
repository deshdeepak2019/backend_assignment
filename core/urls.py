from django.urls import include, path

from core.router import router

urlpatterns = [
    path("", include(router.urls)),
]
