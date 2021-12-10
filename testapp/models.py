from django.db import models

class Parameter(models.Model):
    name = models.CharField(max_length=300)
    value = models.CharField(max_length=300)

class HttpCall(models.Model):
    url = models.URLField()
    time = models.DateTimeField()
    parameters = models.ForeignKey(Parameter, on_delete=models.CASCADE)