from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.template.loader import render_to_string
import os
from django.db.models.loading import get_model
from django.http import Http404
from models.variants import *
from django.template import RequestContext, loader
from models.interventions import Intervention

def interventions(request): return render(request, 'interventions.html')

#def index(request): return render(request, 'index.html')
# def index(request): return render(request, 'interventions.html')
#
# class Intervention(models.Model):
#     name = models.CharField(max_length=250)
#     taxid = models.IntegerField(blank=True, null=True)
#     species = models.ForeignKey('annotations.Species', blank=True, null=True)
#     sex = models.CharField(max_length=25, blank=True)
#     gender = models.ManyToManyField('Gender', blank=True, null=True)
#     background = models.CharField(max_length=250, blank=True)
#     strain = models.ForeignKey('Strain', blank=True, null=True)
#     effect = models.TextField(blank=True)
#     mean = models.CharField(max_length=15, null=True, blank=True)
#     median = models.CharField(max_length=15, null=True, blank=True)
#     maximum = models.CharField(max_length=15, null=True, blank=True)
#     _25 = models.CharField(max_length=15, null=True, blank=True)
#     _75 = models.CharField(max_length=15, null=True, blank=True)
#     manipulation = models.ManyToManyField(Manipulation, blank=True)
#     pmid = models.CharField(max_length=250, blank=True)
#     references = models.ManyToManyField('datasets.Reference', blank=True)
#     lifespans = models.CharField(max_length=25, blank=True)


def index(request):
    ivs = [
        {
            "name":i.name,
            "species":i.species.common_name,
            "manipulation":i.manipulation,
            "maximum":i.maximum,}
        for  i in Intervention.objects.all()
        if i.species!=None
    ]

    context = RequestContext(request,{
        "interventions": ivs,
    })
    return render(request, 'test.html',context)



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


