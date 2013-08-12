from models import *

from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.template.loader import render_to_string
import os
from django.db.models.loading import get_model
from django.http import Http404
from django.template import RequestContext, loader,Context



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

from bulbs.rexster import Graph
from bulbs.rexster import Config
from bulbs.model import *

#
# def index(request):
#     context = Context({
#         })
#     conf = Config("http://localhost:8182/graphs/denigma", username="antonkulaga", password="mind2mind")
#     g = Graph(conf)
#     # james = g.vertices.create(name="James")
#     # julie = g.vertices.create(name="Julie")
#     # g.edges.create(james, "knows", julie)
#     den = g.vertices.get("#9:0")
#     e = den.outE
#     context = Context({
#         "V": den,#g.V, #g.vertices.index.lookup(name="James"),
#         "E": e
#         })
#     return render(request, 'index.html',context)
