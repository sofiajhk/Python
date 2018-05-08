from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 1
    if request.method == 'POST':
        request.session['word'] = get_random_string(length=14)
        request.session['attempt'] += 1
    return render(request, "word_app/index.html")

def reset(request):
    if request.method == 'POST':
        try:
            del request.session['attempt']
            del request.session['word']
            print "everything has been reset!"            
            return redirect('/')
        except KeyError:
            print "you already reset, silly!"
            return redirect('/')

