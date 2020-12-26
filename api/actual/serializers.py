from rest_framework import serializers

from .models import User, Toon, Campaign


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', )


class ToonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toon
        fields = ('toon_name', 'toon_id', 'toon_sprite', 'campaigns', )


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('camp_name', 'encounter', )

class GridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grid
        fields = ('camp', 'name', )

