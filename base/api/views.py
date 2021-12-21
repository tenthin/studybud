from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])  #http methods that are allowed to access the views, we can use 'PUT','POST'
def getRoutes(request):
    routes = [
        'GET/api',
        'GET/api/rooms',
        'GET/api/rooms/:id'
    ]
    return Response(routes)