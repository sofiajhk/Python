from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# read up on documentation on flash messaging in platform (django-model validations)
from models import *

# Create your views here.
def index(request):
    print "Somone is registering or logging in!"
    return render(request, "login_register/index.html")

def reg_process(request):
    result = User.objects.register_validator(request.POST)
    print result

    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect('/')
    
    # if no errors to print run this...
    request.session['user_id'] = result.id
    messages.success(request, "Sucessfully registered!")
    return redirect("/success")


def log_process(request):
    result = User.objects.login_validator(request.POST)
    print result
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect('/')
    
    # if no errors to print run this...
    request.session['user_id'] = result.id
    messages.success(request, "Succesfully logged in!")
    return redirect("/success")


def success(request):
    print "User succesfully registered/signed in!"
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, "login_register/success.html", context)

def logout(request):
    del request.session['user_id']
    print "User succesfully logged out!"
    return redirect('/')
