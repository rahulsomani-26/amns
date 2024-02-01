# Write the function that will be called when the user goes to a particular URL 
# e.g 127.0.0.1:8000/home 


from django.http import HttpResponse
from django.shortcuts import render
# from http.client import HTTPResponse


def startfn(request):
    print("Within the view function ")
    return HttpResponse('<b> This is our first Web Page </b>')

def index(request):
    context = {
        'title':'First Project',
    }
    return render(request,"index.html",context=context)

def getname(request,name):
    return HttpResponse(" Welcome {}".format(name))
