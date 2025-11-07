from django.db import models

class CityTemperature(models.Model):
    # 'city' (CharField, único)
    city = models.CharField(max_length=100, unique=True, verbose_name="Ciudad")

    # 'temperature' (DecimalField)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Temperatura")

    # 'last_updated' (DateTimeField, que se actualice automáticamente)
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return f"{self.city}: {self.temperature}°C"