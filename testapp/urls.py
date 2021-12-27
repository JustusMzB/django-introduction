from django.urls import path
from testapp.views import hello_world, understand_method, hello_name, get_all_calls

app_name = 'testapp'
urlpatterns = [
    path('helloworld/', hello_world, name='hello_world' ),
    path('understandmethod/', understand_method, name = 'understand_method'),
    path('helloname/<str:name>/', hello_name, name='helloname'),
    path('allcalls/', get_all_calls, name='allcalls'),
]