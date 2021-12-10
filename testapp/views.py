import django
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader

# Create your views here.
def hello_world(request):
    return HttpResponse('hello world')
@csrf_exempt
def understand_method(request):
    return HttpResponse('this is a {} - request'.format(request.method))
def hello_name(request, name):
   template = loader.get_template('testapp/helloname.html')
   name = list(name)
   context = {'name':name}
   return HttpResponse(template.render(context, request))
