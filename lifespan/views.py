from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.template import Context, loader
from django.http import HttpResponse
import json
from django.core import serializers


import random

from lifespan.models import Member



def chat(request):
    num = str(random.randint(1, 999))
    username = "guest" +num
    password = "somewrongpassword"
    template = loader.get_template('chat.html')
    context = Context({
        'username': username,
        'password':password,
        })
    return HttpResponse(template.render(context))


def index(request):
    template = loader.get_template('interventions.html')
    context = Context({

        })

    return HttpResponse(template.render(context))


def table(request):
    template = loader.get_template('table.html')
    context = Context({

    })
    return HttpResponse(template.render(context))


def load_table(request):
    #Member.objects.all().delete()
    #Member.objects.filter(id==id).delete()
    # for i in range(0,10):
    #     name = "username_"+str(i)
    #     surname = "surname_"+str(i)
    #     user = Member(name=name, surname=surname, organization="Denigma", age=10 + i, salary=i * 1000)
    #     user.save()
    data = serializers.serialize("json", Member.objects.all())
    return HttpResponse( data )
