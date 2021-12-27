import datetime
from django import template
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from testapp.models import HttpCall, Parameter

def request_into_db(request: HttpRequest):
    call = HttpCall(url = request.path)
    call.save()
    for i in request.GET.items():
        call.parameter_set.create(name = i[0], value = i[1])
    call.save()
# Create your views here.
def hello_world(request):
    request_into_db(request)
    return HttpResponse('hello world')
@csrf_exempt
def understand_method(request):
    return HttpResponse('this is a {} - request'.format(request.method))
def hello_name(request, name):
    request_into_db(request)
    template = loader.get_template('testapp/helloname.html')
    context = {'name':name}
    return HttpResponse(template.render(context, request))
def get_all_calls(request):
    template = loader.get_template('testapp/allcalls.html')
    context = {'httpcalls' : HttpCall.objects.all()}
    return HttpResponse(template.render(context, request))