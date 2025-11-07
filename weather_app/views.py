from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import CityTemperature
from .serializers import CityTemperatureSerializer

class CityTemperatureViewSet(viewsets.ModelViewSet):
    """
    Este ViewSet provee automáticamente las acciones:
    .list()    (GET /api/temperatures/)
    .retrieve() (GET /api/temperatures/1/)
    .create()  (POST /api/temperatures/)
    .update()  (PUT /api/temperatures/1/)
    .destroy() (DELETE /api/temperatures/1/)
    """
    queryset = CityTemperature.objects.all().order_by('city')
    serializer_class = CityTemperatureSerializer

    # Los permisos ya están globales, pero es buena práctica repetirlos aquí
    permission_classes = [IsAuthenticatedOrReadOnly]