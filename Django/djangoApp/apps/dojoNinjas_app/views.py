from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Hello, this is your users app!"
    return HttpResponse(response)
