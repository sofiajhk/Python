from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# index method @ '/' route: display "placeholder to later display all the list of blogs" via HttpResponse
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

# new method @ '/new' route: display "placeholder to display a new form to create a new blog" via HttpResponse. 
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

# create method @ '/create' route: have this url redirect to '/'
def create(request):
    return redirect('/')

# show method @ '/{{number}}' route: display "placeholder to display blog {{number}}".  
# For example '/15' should display a message "placeholder to display blog 15"
def show(request, number):
    return HttpResponse("placeholder to display blog #" + number)


# edit method @ '/{{number}}/edit' route: display "placeholder to edit blog {{number}}"
def edit(request, number):
    return HttpResponse("placeholder to edit blog #" + number)

# destroy method @ '/{{number}}/delete' route: have this url redirect to '/'
def destroy(request, number):
    return redirect('/')

