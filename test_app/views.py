from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def greetings(request:HttpRequest) -> HttpResponse:
    return HttpResponse('Hello, Ruslan!')
