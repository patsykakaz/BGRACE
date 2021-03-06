#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from itertools import chain

from django.utils.translation import ugettext as _

from mezzanine.pages.page_processors import processor_for
from mezzanine.core.request import current_request
from mezzanine.blog.models import BlogPost
from .models import *
from forms import ContactForm

@processor_for('/')
def processor_home(request, page):
    Boats = Boat.objects.exclude(occasion=True)
    BlogPost_highlights = BlogPost.objects.filter(highlight=True)[:3]
    Boat_highlights = Boat.objects.filter(highlight=True)[:3]
    highlights = sorted(chain(BlogPost_highlights,Boat_highlights))
    last_blogPosts = BlogPost.objects.exclude(id__in=BlogPost_highlights)[:3]
    distrib_pays_list = []
    for element in Distributeur.objects.all():
        if element.pays not in distrib_pays_list:
            distrib_pays_list.append(element.pays)
    bassins_navigation = BassinNav.objects.all()
    return locals()

@processor_for(Boat)
def processor_boat(request, page):
    boat = Boat.objects.get(id=page.id)
    illustrations = BoatGalery.objects.filter(Boat=boat)
    palmares_all = BoatPalmares.objects.filter(Boat=boat)
    documentation_all = BoatDocumentation.objects.filter(Boat=boat)
    form = ContactForm()
    return locals()


@processor_for('occasions')
def processor_occasions(request, page):
    occasions = Boat.objects.filter(occasion=True)
    for element in occasions:
        element.illustrations = BoatGalery.objects.filter(Boat=element)
    return locals()

@processor_for(Distributeur)
def processor_distributeur(request, page):
    page = Distributeur.objects.get(id=page.id)
    form = ContactForm()
    return locals()

@processor_for('distributeurs')
def processor_distributeurs(request, page):
    distrib_pays_list = []
    for element in Distributeur.objects.all():
        if element.pays not in distrib_pays_list:
            distrib_pays_list.append(element.pays)
    bassins_navigation = BassinNav.objects.all()
    if not request.POST:
        emptyPostData = True
    elif request.POST:
        if 'bassinNav' in request.POST:
            distributeurs = Distributeur.objects.filter(bassin_navigation=BassinNav.objects.get(pk=int(request.POST['bassinNav'])))
        elif 'country' in request.POST:
            distributeurs = Distributeur.objects.filter(pays=request.POST['country'])
        else:
            error = True
    return locals()
