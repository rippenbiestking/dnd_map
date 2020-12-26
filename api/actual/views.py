from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .models import User, Toon
from.serializers import UserSerializer, ToonSerializer, CampaignSerializer


@api_view(['GET', ])
def user(request):
    user = User.objects.create()
    serializer = UserSerializer(instance=user)
    return Response(serializer.data)


class ToonViewSet(viewsets.ModelViewSet):
    serializer_class = ToonSerializer

    def get_queryset(self):
        return self.request.uid.toon_set

    def create(self, request):
        print(request.data)
        toon = Toon.objects.create(user=request.uid, toon_name=request.data['toon_name'], toon_sprite=request.data['toon_sprite'])
        serializer = self.serializer_class(instance=toon)
        return Response(serializer.data)


class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
