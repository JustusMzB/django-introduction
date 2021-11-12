from django.urls import path
from testapp.views import hello_world, understand_method

app_name = 'testapp'
urlpatterns = [
    path('helloworld/', hello_world, name='hello_world' ),
    path('understandmethod/', understand_method, name = 'understand_method')
]