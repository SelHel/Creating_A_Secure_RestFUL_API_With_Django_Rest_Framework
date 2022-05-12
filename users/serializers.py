from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    """Conversion des données du modèle User au format JSON."""

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
