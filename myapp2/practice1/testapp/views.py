from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first(request):
    return HttpResponse("first")


def second(request):
    return HttpResponse("second")


def third(request):
    return HttpResponse("third")


def fourth(request):
    return HttpResponse("fourth")


def login(request):
    return render(request, 'base.html')


def result(request):
    # username = request.GET['username']
    return render(request, 'login/result.html')
