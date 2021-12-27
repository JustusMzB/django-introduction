from django.db import models

class HttpCall(models.Model):
    url = models.URLField()
    def __str__(self):
        return self.url
    

class Parameter(models.Model):
    name = models.CharField(max_length=300)
    value = models.CharField(max_length=300)
    call = models.ForeignKey(HttpCall, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}={self.value}'