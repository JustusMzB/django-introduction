from django.db import models

class HttpCall(models.Model):
    url = models.URLField()

class Parameter(models.Model):
    name = models.CharField(max_length=300)
    value = models.CharField(max_length=300)
    parameters = models.ForeignKey(HttpCall, on_delete=models.CASCADE)