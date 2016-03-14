#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
# from django.contrib.sites.models import *

from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.utils.models import upload_to


class HiddenPage(Page):
    # excluded from Nav/Footer
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # in_menus empty -> exclude from content_trees
        self.in_menus = []
        super(HiddenPage, self).save(*args, **kwargs)

class Boat(Page):
    highlight = models.NullBooleanField(default=False,null=True, blank=True,verbose_name='mettre en avant sur la HomePage')
    baseline = models.CharField(max_length=255, null=True, blank=True, verbose_name='baseline/modèle',help_text='Baseline si modèle neuf, nom du modèle si bateau d\'occasion')
    occasion = models.NullBooleanField(default=False, null=True, blank=False)
    price = models.CharField(max_length=255,default='non spécifié', null=True, blank=True, verbose_name='prix', help_text='pour bateau occasion uniquement')
    annee_construction = models.CharField(max_length=255, null=True, blank=True, help_text='pour bateau occasion uniquement')
    featured_image = FileField(verbose_name=_("Image en situation"),
        upload_to=upload_to("MAIN.Boat", "Boat"),
        format="Image", max_length=255, null=True, blank=False)
    sidecut_image = FileField(verbose_name=_("Plan de coupe"),
        upload_to=upload_to("MAIN.Boat", "Boat"),
        format="Image", max_length=255, null=True, blank=True)
    sidecut_image_2 = FileField(verbose_name=_("Plan de coupe avec voile"),
        upload_to=upload_to("MAIN.Boat", "Boat"),
        format="Image", max_length=255, null=True, blank=True)
    logo = FileField(verbose_name=_("Logo Bateau"),
        upload_to=upload_to("MAIN.Boat", "Boat"),
        format="Image", max_length=255, null=True, blank=True)
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
    lest = models.CharField(max_length=255, 
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

    def save(self, *args, **kwargs):
        # in_menus empty -> exclude from content_trees
        if self.occasion == True :
            self.in_menus = []
        else:
            self.in_menus = ['1']
        super(Boat, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'BATEAU'

class BoatGalery(models.Model):
    Boat = models.ForeignKey("Boat")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("MAIN.Boat", "Boat"),
        format="Image", max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    display_size = models.IntegerField(default=6,help_text='taille de l\'image. Entrez un nombre pair, entre 2 et 12.',null=True, blank=True)

    class Meta:
        verbose_name = 'GALLERIE (BATEAU)'

class BoatDocumentation(models.Model):
    Boat = models.ForeignKey("Boat")
    fileTarget = models.FileField(upload_to='boat/doc/')
    doc_nature_choices = (
        ('',''),
        ('Présentation', 'Présentation'),
        ('VPP', 'VPP'),
        ('Courbe de stabilité ', 'Courbe de stabilité '),
        ('Règle de classe ', 'Règle de classe '),
        ('Caractéristiques techniques détaillées', 'Caractéristiques techniques détaillées'),
        ('Plan d’aménagement', 'Plan d’aménagement'),
        ('Options', 'Options'),
    )
    doc_nature = models.CharField(max_length=50, 
                    choices=doc_nature_choices, null=True, blank=True)
    alternative_doc_nature = models.CharField(max_length=255,
                                            null=True, blank=True)

    class Meta:
        verbose_name = 'DOCUMENTATION (BATEAU)'

class BoatPalmares(models.Model):
    Boat = models.ForeignKey("Boat")
    year = models.CharField(max_length=6, verbose_name='année')
    course = models.CharField(max_length=255)
    resultat = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'PALMARES (BATEAU)'


class BassinNav(Page):
    def save(self, *args, **kwargs):
        # in_menus empty -> exclude from content_trees
        self.in_menus = []
        super(BassinNav, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        # in_menus empty -> exclude from content_trees
        self.in_menus = []
        super(BassinNav, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'BASSIN de NAVIGATION'

class Distributeur(Page):
    illustration = FileField(verbose_name=_("Illustration"),
        upload_to=upload_to("MAIN.Distributeur", "illustration"),
        format="Image", max_length=255, null=True, blank=True)
    logo = FileField(verbose_name=_("Logo"),
        upload_to=upload_to("MAIN.Distributeur", "Distributeur"),
        format="Image", max_length=255, null=True, blank=True)
    bassin_navigation = models.ManyToManyField("BassinNav")
    pays = models.CharField(max_length=255,null=False, blank=True)
    presentation = RichTextField(_("Presentation"))
    nom = models.CharField(max_length=255, null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)
    tel = models.CharField(max_length=255, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    horaires = models.TextField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        # in_menus empty -> exclude from content_trees
        self.in_menus = []
        super(Distributeur, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'DISTRIBUTEUR'




