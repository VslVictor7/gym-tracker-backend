from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('id','username', 'email', 'password', 'first_name', 'last_name')
        