import django
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def hello_world(request):
    return HttpResponse('hello world')
@csrf_exempt
def understand_method(request):
    return HttpResponse('this is a {} - request'.format(request.method))
