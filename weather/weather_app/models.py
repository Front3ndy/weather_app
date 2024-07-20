from django.db import models


class TempTable(models.Model):
    ip = models.CharField(max_length=15)
    cities = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.ip} - {self.cities}'
