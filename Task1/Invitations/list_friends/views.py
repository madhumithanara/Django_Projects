from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Friend
import math
from django.core.exceptions import *

def cos(num):
    to_rad = (num/180)*math.pi
    return math.cos(to_rad)

def inputting(response):
    template = loader.get_template('list_friends/input.html')
    context = {}
    return HttpResponse(template.render(context, response))

def result(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
    coord = search_id.split()

#def index(response):
    all_people = Friend.objects.all()

    lat = float(coord[0])
    longt = float(coord[1])
    x = float(coord[2])

    names = [[]]

    for person in all_people:
        person.user_id = int(person.user_id)

        plat = float(person.latitude)
        plong = float(person.longitude)
        dist = math.sqrt((((lat-plat)*110.574)**2 + (((longt*111.320*cos(lat))-(plong*111.320*cos(plat))))**2))

        if dist < x:
            dist = round(dist,2)
            names.append([person.name,dist,person.user_id])



    names.pop(0)
    names = sorted(names, key=lambda x : x[2])

    invited = []
    for name in names:
        temp = {"name":name[0],
                 "distance": name[1],"user_id":name[2]}
        invited.append(temp)


    template = loader.get_template('list_friends/index.html')
    context = {
        'invited':invited,
    }


    return HttpResponse(template.render(context, request))
    #return HttpResponse(names)

def index(response):
    return HttpResponse("Look at /input")