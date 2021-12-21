from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer
from base.api import serializers

@api_view(['GET'])  #http methods that are allowed to access the views, we can use 'PUT','POST'
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all() #python list of objects
    serializers = RoomSerializer(rooms, many=True)
    return Response(serializers.data)