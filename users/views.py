from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.db.models import Q
from rest_framework_simplejwt.views import TokenObtainPairView
from ais.permissions import UserCanCreate
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from .models import CustomUser


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class GetCurrentUser(APIView):
    """
    Получить текущего пользователья
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class GetRelatedUser(APIView):
    """
    Получить связанного пользователья
    """

    permission_classes = [permissions.IsAuthenticated, UserCanCreate]

    def get(self, request):
        if not request.user.is_superuser:
            users = CustomUser.objects.filter(Q(groups__in=request.user.groups.all()) & Q(is_contractor=True))
            serializer = UserSerializer(users, many=True)
        else:
            users = CustomUser.objects.filter(Q(is_contractor=True)).all()
            serializer = UserSerializer(users, many=True)

        return Response(serializer.data)
