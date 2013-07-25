from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.template.loader import render_to_string
import os
from django.db.models.loading import get_model
from django.http import Http404


def index(request): return render(request, 'interventions.html')

def writeModel(request, app, model):
    model = model.title()
    filename = model+".coffee"
    path = os.path.abspath(app+"/coffee/models/" + filename.lower())
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
        "app": app,
        "storage":"Batman.RestStorage",
        "fields": fields,
        "storage_key":key
    })
    open(path, "w").write(render_to_string(template_name, context))
    return HttpResponse(template.render(context), mimetype="application/json")
    #return  render(request,"model.coffee.html",context)


