from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat1(request):
    return HttpResponse('This is virat1 page')
def virat2(request):
    return render(request,'virat.html')
