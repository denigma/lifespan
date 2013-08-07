# -*- coding: utf-8 -*-
import re

from django.db import models, IntegrityError
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models.signals import m2m_changed
from django.core.urlresolvers import reverse
from time import strptime
from datetime import datetime
import handlers
from mptt.models import MPTTModel, TreeForeignKey
from lifespan.models.interventions import Factor

t_prefix = "lifespan_"

class VariantManager(models.Manager):
    def get_queryset(self):
        return self.model.objects.exclude(choice__name__contains='Review')


class StateManager(models.Manager):
    def get_queryset(self):
        print("get queryset")
        return self.model.objects.exclude(variant__choice__name__contains='Review')


class State(models.Model):
    name = models.CharField(max_length=250)

    objects = StateManager()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('state', args=[self.pk])

    class Meta():
        db_table = t_prefix+"state"



class Technology(models.Model): # PCR, array
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('technology', args=[self.pk])

    class Meta:
        verbose_name_plural = 'Technologies'
        db_table = t_prefix+"technology"


class StudyType(models.Model): # GWAS, Candidate genes
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('study_type', args=[self.pk])

    class Meta():
        db_table = t_prefix+"studytype"


class Population(MPTTModel):
    name = models.CharField(max_length=250)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('population', args=[self.pk])

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta():
        db_table = t_prefix+"population"


# class Association(models.Model):
#     def __unicode__(self):
#         return self.polymorphism


class VariantType(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Variant Type'
        verbose_name_plural = 'Variant Types'
        db_table = t_prefix+"varianttype"


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('variant_type', args=[self.pk])



class ORType(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Odds ratio Type'
        verbose_name_plural = 'Odds ratio Types'
        db_table = t_prefix+"ortype"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('or_type', args=[self.pk])




class Variant(models.Model):

    CHOICES = (
        (1, _('Positive')),
        (2, _('Negative')),
        #    (3, _('Multiplicative'))
    )

    finding = models.PositiveSmallIntegerField(max_length=1, blank=True, null=True, choices=CHOICES,
                                               help_text="Whether finding was positive or negative.")
    #polymorphism = models.CharField(max_length=20)# genetic variant
    created = models.DateTimeField(_('created'), auto_now_add=True, db_index=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    location  = models.CharField(max_length=10, null=True, blank=True)# genomic location
    factor = models.ForeignKey(Factor, null=True, blank=True, related_name='variants')
    shorter_lived_allele = models.CharField(max_length=255, blank=True, null=True)
    longer_lived_allele = models.CharField(max_length=255, blank=True, null=True)
    variant_type = models.ForeignKey('VariantType', blank=True, null=True)
    or_type = models.ForeignKey('ORType', help_text='Odds Ratio Type', blank=True, null=True)


    polymorphism = models.CharField(max_length=255)# genetic variant
    alias = models.CharField(max_length=255, blank=True, null=True,
                             help_text='Individual alias names should be seperated by semicolon ";"')
    #variants = models.ManyToManyField(Variant)
    factors = models.ManyToManyField(Factor, null=True, blank=True, related_name='variances')
    description = models.TextField(null=True, blank=True)
    odds_ratio = models.FloatField(null=True, blank=True)
    pvalue = models.FloatField(null=True, blank=True, help_text="Numerical value of the p-value")
    p_value = models.CharField(max_length=255, null=True, blank=True, help_text="String representation of the p-value, e.g. > 0.05 (females)")# genetic variant
    qvalue = models.FloatField(null=True, blank=True)
    significant = models.CharField(max_length=255, null=True, blank=True)  # (redudant)
    initial_number = models.CharField(max_length=250, null=True, blank=True) # _of_cases_controls (study)
    replication_number = models.CharField(max_length=250, null=True, blank=True) #     _of_cases_controls (study)
    ethnicity = models.ManyToManyField(Population)# German
    age_of_cases = models.CharField(max_length=250, null=True, blank=True)
    study_type = models.ForeignKey(StudyType, null=True, blank=True)    # GWAS, Candidate genes
    technology = models.ForeignKey(Technology, null=True, blank=True)     # PCR, array
    pmid = models.IntegerField(blank=True, null=True)
    reference = models.ForeignKey('datasets.Reference')
    choice = models.ForeignKey(State, default=1, null=True, blank=True) #[Curate/Review/Discard]
    classifications = models.ManyToManyField('annotations.Classification', blank=True, null=True, default=None)

    objects = VariantManager()

    def __unicode__(self):
        return self.polymorphism

    def get_absolute_url(self):
        return reverse('variant', args=[self.pk])



m2m_changed.connect(handlers.changed_references, sender=Factor.references.through)