from django.urls import path
from.views import simpleView

urlpatterns  =  [   
    path('', simpleView, name='home'),
]