from django.db import models

class HttpCall(models.Model):
    url = models.URLField()
    #def __str__(self):
        #return f'{self.url} at {self.time} with params { list(self.parameter_set.all())}'

class Parameter(models.Model):
    name = models.CharField(max_length=300)
    value = models.CharField(max_length=300)
    call = models.ForeignKey(HttpCall, on_delete=models.CASCADE)
    #def __str__(self):
        #return f'{self.name}={self.value}'