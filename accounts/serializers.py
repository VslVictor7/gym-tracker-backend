from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        exclude = [
            'password',
            'groups',
            'user_permissions',
            'is_staff',
            'is_active',
            'date_joined',
            'last_login',
            'is_superuser',
        ]
        