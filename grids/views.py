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
from grids.models import Member, Organization
from lookups import *


from django.views.generic import TemplateView


class CoffeeModelView(TemplateView):


    model_name = "no_model"
    namespace = "grids"
    template_name = "model.coffee.html"
    content_type='application/json'
    #template_name = "grid.html"

    def get_context_data(self, **kwargs):

        model = self.model_name.title()
        key = model.lower()
        modelClass = get_model(self.namespace,model)
        if not modelClass:
            raise Http404
        models = modelClass.objects.all()
        fields = models[0].keys()
        context = kwargs
        if 'view' not in context:
            context['view'] = self
        context["model"] = model
        context["fields"] = fields
        context["title"] = model
        context["storage"] ="Batman.RestStorage"
        context["fields"] = fields
        context["storage_key"] = key
        return context


class GridView(TemplateView):

    namespace = "grids"
    model_name = "no_model"
    #template_name = "model.coffee.html"
    template_name = "grid.html"

    def get_context_data(self, **kwargs):

        model = self.model_name.lower()
        #template = loader.get_template('grid.html')
        modelClass = get_model(self.namespace, model)
        if not modelClass:
            raise Http404
        models = modelClass.objects.all()
        fields = models[0].keys()

        context = kwargs
        if 'view' not in context:
            context['view'] = self
        context["model"] = model
        context["fields"] = fields
        return context

#just a test class to experiment with lookups
class SelectableGridView(GridView):
    def get_context_data(self, **kwargs):
        context =  GridView.get_context_data(self, **kwargs)
        context["form"] = OrganizationForm()
        return context


def fixture(request):
    """Used it only to generate fixture data"""
    Organization.objects.all().delete()
    denigma = Organization(name="Denigma",description="Digital Enigma for ageing research")
    ILA = Organization(name="ILA",description="International Longevity Alliance")
    cloud_mice = Organization(name="Cloud mice",description="Cloud mice testing center")
    orgs = [denigma,ILA,cloud_mice]
    for org in orgs:
        org.save()

    Member.objects.all().delete()
    for i in range(0,100):
        name = "username_"+str(i)
        surname = "surname_"+str(i)
        user = Member(name=name, surname=surname, organization=orgs[i%len(orgs)], age=10 + i, salary=i * 1000)
        user.save()
    models = Member.objects.all()
    #data = {"fields":models[0].keys(),"values":[model.values() for model in models]}
    data = [model.items() for model in models]
    #return render(json.dumps(data), mimetype="application/json")
    path = os.path.abspath("grids/fixtures/" + "initial_data.json")
    js = json.dumps(data)
    open(path, "w").write(js)
    return HttpResponse( js, mimetype="application/json")