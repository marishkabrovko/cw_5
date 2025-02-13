from rest_framework.serializers import ModelSerializer

# from rest_framework import serializers
from users.models import User

# from users.validators import validate_telegram_nick


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
