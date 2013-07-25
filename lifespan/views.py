import random

from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
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
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from lifespan.serializers import MemberSerializer

def index(request): return render(request, 'interventions.html')


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


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


