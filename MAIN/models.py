#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
# from django.contrib.sites.models import *

from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField

class HiddenPage(Page):
    # excluded from Nav/Footer
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # in_menus empty -> exclude from content_trees
        self.in_menus = []
        super(Publicite, self).save(*args, **kwargs)

class Boat(HiddenPage):
    headline = models.CharField(max_length=255, null=True, blank=True)
    illustration = models.ImageField(upload_to=settings.MEDIA_ROOT
                                        +'/boat/illustration', null=False)
    logo_boat = models.ImageField(upload_to=settings.MEDIA_ROOT
                                        +'/boat/logo_boat', null=False)
    documentation = models.FileField(upload_to='boat/doc/')
    presentation = RichTextField(_("Presentation"))

    architecte = models.CharField(max_length=255, 
                                    null=True, blank=True)
    longueur_HT = models.CharField(max_length=255, 
                                    null=True, blank=True)
    longueur_coque = models.CharField(max_length=255, 
                                    null=True, blank=True)
    largeur = models.CharField(max_length=255, 
                                    null=True, blank=True)
    tirant_eau = models.CharField(max_length=255, 
                                    null=True, blank=True)
    deplacement = models.CharField(max_length=255, 
                                    null=True, blank=True)
    leste = models.CharField(max_length=255, 
                                    null=True, blank=True)
    surface_voile = models.CharField(max_length=255, 
                                    null=True, blank=True)
    spi = models.CharField(max_length=255, 
                                    null=True, blank=True)
    motorisation = models.CharField(max_length=255, 
                                    null=True, blank=True)
    capacite_carburant = models.CharField(max_length=255, 
                                    null=True, blank=True)
    capacite_eau = models.CharField(max_length=255, 
                                    null=True, blank=True)
    cabines = models.CharField(max_length=255, 
                                    null=True, blank=True)
    certification_CE = models.CharField(max_length=255, 
                                    null=True, blank=True)
    association_classe = models.CharField(max_length=255, 
                                    null=True, blank=True)

class BoatDocumentation(models.Model):
    Boat = models.ForeignKey("Boat")
    fileTarget = models.FileField(upload_to='boat/doc/')
    doc_nature_choices = (
        ('', ''),
        ('Présentation', 'Présentation'),
        ('VPP', 'VPP'),
        ('Courbe de stabilité ', 'Courbe de stabilité '),
        ('Règle de classe ', 'Règle de classe '),
        ('Caractéristiques techniques détaillées ', 'Caractéristiques techniques détaillées '),
        ('Plan d’aménagement', 'Plan d’aménagement'),
        ('Options', 'Options'),
    )
    doc_nature = models.CharField(max_length=50, 
                    choices=doc_nature_choices,
                    default='')
    alternative_doc_nature = models.CharField(max_length=255,
                                            null=True, blank=True)

class BoatPalmares(models.Model):
    Boat = models.ForeignKey("Boat")
    year = models.DateField()
    course = models.CharField(max_length=255)
    resultat = models.CharField(max_length=255)











