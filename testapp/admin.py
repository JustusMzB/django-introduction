from django.contrib import admin
from .models import HttpCall, Parameter

admin.site.register([HttpCall, Parameter])
