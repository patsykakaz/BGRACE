#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from itertools import chain

from mezzanine.pages.page_processors import processor_for
from mezzanine.core.request import current_request
from mezzanine.blog.models import BlogPost
from .models import *

@processor_for('/')
def processor_home(request, page):
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
def processor_home(request, page):
    boat = Boat.objects.get(title=page.title)
    return locals()