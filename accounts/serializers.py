from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('id','username', 'email', 'password', 'first_name', 'last_name')
        