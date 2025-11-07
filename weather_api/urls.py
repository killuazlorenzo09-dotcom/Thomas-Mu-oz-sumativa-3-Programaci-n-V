from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as authtoken_views
# Importamos las vistas de la app
from weather_app import views as temp_views 

# Cree el router
router = DefaultRouter()

# Registre las vistas (el ViewSet) con el router
# Esto crea las URLs de CRUD automáticamente
router.register(r'temperatures', temp_views.CityTemperatureViewSet, basename='temperature')

# Definimos las URLs del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),

    # Incluimos las URLs generadas por el router en la ruta 'api/'
    path('api/', include(router.urls)),

    # Endpoint para que los usuarios obtengan su token de autenticación
    path('api/get-token/', authtoken_views.obtain_auth_token, name='get-token'),
]