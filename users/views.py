from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from users.serializers import UserSerializer


class CreateUserAPIView(APIView):
    """Vue qui permet à l'utilisateur d'accéder à une URL pour créer un compte."""

    permission_classes = [AllowAny]
    # Autorise tous les utilisateurs (authentifiés ou non) à accéder à cette url.

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
