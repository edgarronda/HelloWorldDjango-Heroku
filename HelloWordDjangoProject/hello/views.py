import re
from datetime import datetime
#from django.shortcuts import render
from django.http import HttpResponse

#https://code.visualstudio.com/docs/python/tutorial-django

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django. Fuck Yhea!")

def hello_there(request, name):
    CrrntDateTime = datetime.now()
    DateTimeParsed = CrrntDateTime.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
        pass
    else:
        clean_name = "Friend"
        pass
    
    content = "Hello there, " + clean_name + "! It's " + DateTimeParsed

    return HttpResponse(content)
