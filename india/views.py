from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def india1(request):
    return HttpResponse('this is india branch page')
def india2(request):
    return render(request,'sachin.html')
