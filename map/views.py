from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from tasks.models import Task
from geojson import MultiPoint
from .serializers import GetTaskToMapSerialize


class GetGeoJson(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        location = list()
        queryset = Task.objects.all()

        for i in queryset:
            location.append([i.longitude, i.latitude])

        gjs = MultiPoint(location, precision=20)

        return Response(gjs)


class GetTaskToMap(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        lat = request.query_params['lat']
        lng = request.query_params['lng']
        queryset = Task.objects.filter(latitude=lat, longitude=lng).all()

        serializer = GetTaskToMapSerialize(queryset, many=True)

        return Response(serializer.data)
