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

def index(request):
    model = "Member".lower()
    #template = loader.get_template('grid.html')
    modelClass = get_model("lifespan",model)
    models = modelClass.objects.all()
    fields = models[0].keys()
    context = Context({
        "model": model,
        "fields": fields,
        })
    #return HttpResponse(template.render(context))
    return render(request, 'grid.html',context)


def writeModel(request,model):
    model = model.title()
    filename = model+".coffee"
    path = os.path.abspath("coffee/models/" + filename.lower())
    template_name = "model.coffee.html"
    template = loader.get_template(template_name)
    key = model
    modelClass = get_model("lifespan",model)
    if not modelClass:
        raise Http404
    models = modelClass.objects.all()
    fields = models[0].keys()
    context = RequestContext({
        "name": model,
        "storage":"Batman.RestStorage",
        "fields": fields,
        "storage_key":key
    })
    open(path, "w").write(render_to_string(template_name, context))
    return HttpResponse(template.render(context), mimetype="application/json")
    #return  render(request,"model.coffee.html",context)


def members(request):
    # Member.objects.all().delete()
    # for i in range(0,100):
    #     name = "username_"+str(i)
    #     surname = "surname_"+str(i)
    #     user = Member(name=name, surname=surname, organization="Denigma", age=10 + i, salary=i * 1000)
    #     user.save()
    models = Member.objects.all()
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