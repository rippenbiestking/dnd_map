from rest_framework import serializers

from .models import User, Toon


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', )


class ToonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toon
        fields = ('toon_name', 'toon_id', 'toon_sprite', )
