from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.template import Context, loader
from django.http import HttpResponse
import json
from django.core import serializers
from lifespan.models import Member
import random
from django.forms.models import model_to_dict
from django.template.loader import render_to_string
from django.conf import settings
import os
from django.db.models.loading import get_model
from django.http import Http404


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
    # Member.objects.all().delete()
    # for i in range(0,100):
    #     name = "username_"+str(i)
    #     surname = "surname_"+str(i)
    #     user = Member(name=name, surname=surname, organization="Denigma", age=10 + i, salary=i * 1000)
    #     user.save()
    models = Member.objects.all()
    #data = {"fields":models[0].keys(),"values":[model.values() for model in models]}
    data = [models[0].keys()] + [model.values() for model in models]
    return HttpResponse( json.dumps(data) )


def messages(request):
    data = serializers.serialize("json", Member.objects.all())
    return HttpResponse( data )


def writeModel(request,model):
    model = model.title()
    filename = model+".coffee"
    path = os.path.abspath("static/models/" + filename)
    template_name = "model.coffee.html"
    template = loader.get_template(template_name)
    key = model
    modelClass = get_model("lifespan",model)
    if not modelClass:
        raise Http404
    models = modelClass.objects.all()
    fields = models[0].keys()
    context = Context({
        "name": model,
        "storage":"Batman.RestStorage",
        "fields": fields,
        "storage_key":key
    })
    open(path, "w").write(render_to_string(template_name, context))
    return HttpResponse(template.render(context))




