import json

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from lifespan.models import Member
from django.template.loader import render_to_string
import os
from django.db.models.loading import get_model
from django.http import Http404
from django.http import QueryDict
from django.template import RequestContext, loader

@csrf_exempt
def save(request, model, uri):
    if request.method == "PUT":
        params = QueryDict(request.body, request.encoding)
        dic = dict(params.iterlists())
        record = Member(*dic)
        record.save()
        str = model + "/"+uri
    str = model + "/"+uri
    return HttpResponse( str)

def all(request, model):
    modelClass = get_model("lifespan",model)
    models = modelClass.objects.all()
    #data = {"fields":models[0].keys(),"values":[model.values() for model in models]}
    data = [model.items() for model in models]
    #return render(json.dumps(data), mimetype="application/json")
    return HttpResponse( json.dumps(data), mimetype="application/json")


@csrf_exempt
def saveMember(request,id):
    params = QueryDict(request.body, request.encoding)
    model = params
    return render(request)


def blank(request):
    return HttpResponse("this is blank for some reason!")

