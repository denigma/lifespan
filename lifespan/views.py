from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

import random

def chat(request):
    num = str(random.randint(1, 999))
    username = "guest" +num
    password = "somewrongpassword"

    menu = ("item1","ITEM2")
    template = loader.get_template('chat.html')
    context = Context({
        'username': username,
        'password':password,
        'menu': menu,
        })
    return HttpResponse(template.render(context))


def index(request):
    return chat(request)
