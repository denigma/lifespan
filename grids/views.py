import os
import json

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.template.loader import render_to_string

from django.db.models.loading import get_model
from django.http import Http404
from django.http import QueryDict
from django.template import RequestContext, loader

from grids.models import Member


def index(request):
    """Renders grid template,"""
    model = "Member".lower()
    #template = loader.get_template('grid.html')
    modelClass = get_model("grids", model)
    models = modelClass.objects.all()
    #fields = models[0].keys()
    fields = modelClass.keys()
    context = Context({
        "model": model,
        "fields": fields,
        })
    return render(request, 'grid.html',context)

def writeCoffee(request,model):
    """Writes model template to the coffee file."""
    #TODO: check model and controller templates as they may be outdated
    #TODO: add generation for constrains based on fieldtypes for models
    #TODO: add controller generation from controller's template
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
        "title": model,
        "storage":"Batman.RestStorage",
        "fields": fields,
        "storage_key":key
    })
    open(path, "w").write(render_to_string(template_name, context))
    return HttpResponse(template.render(context), mimetype="application/json")
    #return  render(request,"model.coffee.html",context)


def blank(request):
    return HttpResponse("this is blank for some reason!")


def fixture(request):
    """Used it only to generate fixture data"""
    Member.objects.all().delete()
    for i in range(0,100):
        name = "username_"+str(i)
        surname = "surname_"+str(i)
        user = Member(name=name, surname=surname, organization="Denigma", age=10 + i, salary=i * 1000)
        user.save()
    models = Member.objects.all()
    #data = {"fields":models[0].keys(),"values":[model.values() for model in models]}
    data = [model.items() for model in models]
    #return render(json.dumps(data), mimetype="application/json")
    path = os.path.abspath("grids/fixtures/" + "initial_data.json")
    js = json.dumps(data)
    open(path, "w").write(js)
    return HttpResponse( js, mimetype="application/json")