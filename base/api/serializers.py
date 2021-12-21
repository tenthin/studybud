#objects cannot be converted automatically
#take certain model or object and turn it into json data.
#basically turn python object into json object and then we can return later

from rest_framework.serializers import ModelSerializer
from base.models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'