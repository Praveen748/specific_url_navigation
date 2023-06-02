from django.urls import path
from csk.views import *
app_name='csk'
urlpatterns=[
    path('msd1/',msd1,name='msd1'),
    path('msd2/',msd2,name='msd2'),

]