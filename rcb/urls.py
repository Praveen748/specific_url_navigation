from django.urls import path
from rcb.views import *
app_name='rcb'
urlpatterns=[
    path('virat1/',virat1,name='virat1'),
    path('virat2/',virat2,name='virat2'),

]