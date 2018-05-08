from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "survey_app/index.html")

def process(request):
    print "GOT POST INFO"
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
    return redirect('/result')

def result(request):
    return render(request, "survey_app/result.html")

def reset(request):
    if request.method == 'POST':
        try:
            del request.session['name']
            del request.session['location']
            del request.session['language']
            del request.session['comments']
            # check to see if name is still in session
            print "name" in request.session
            print "everything has been reset!"            
            return redirect('/')
        except KeyError:
            print "you already reset, silly!"
            return redirect('/')