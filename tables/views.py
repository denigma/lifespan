from django.views.decorators.csrf import csrf_exempt
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
from django.http import QueryDict


def index(request):
    model = "Member".lower()
    template = loader.get_template('table.html')
    modelClass = get_model("lifespan",model)
    models = modelClass.objects.all()
    fields = models[0].keys()
    context = Context({
        "model": model,
        "fields": fields,
        })
    return HttpResponse(template.render(context))



def data(request):
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
# Create your views here.
