from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index():
    respsone = "navigate to  your models.py in book_authors app to see this assignments"
    return HttpResponse(respsone)