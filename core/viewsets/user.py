from typing import Any

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from core.serializers import UserLoginSerializer, UserRegisterSerializer


class UserViewSet(
    viewsets.GenericViewSet,
):
    """API view set for User model."""

    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    @action(
        methods=["post"],
        detail=False,
        name="login",
    )
    def login(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request=request,
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if user is not None:
            login(request, user)
            response = Response(
                status=status.HTTP_200_OK, data={"details": "Successfully Login"}
            )
            return response

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={"details": "You have enter wrong details"},
        )

    @action(
        methods=["post"],
        detail=False,
        name="register",
        serializer_class=UserRegisterSerializer,
    )
    def register(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if (
            serializer.validated_data["password"]
            != serializer.validated_data["password_again"]
        ):
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"details": "Password Mismatch"},
            )
        try:
            User.objects.get(username=serializer.validated_data["username"])
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "details": "Account with this username already exist, Please choose another user name"
                },
            )
        except User.DoesNotExist:
            User.objects.create_user(
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
            )
        return Response(
            status=status.HTTP_201_CREATED,
            data={"details": "Account Created successfully,Please login"},
        )

    @action(
        methods=["get"],
        detail=False,
        name="logout",
    )
    def logout(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        logout(request)
        return Response(
            status=status.HTTP_200_OK,
            data={"details": "Logout Successfully"},
        )
