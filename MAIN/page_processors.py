#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from itertools import chain

from mezzanine.pages.page_processors import processor_for
from mezzanine.core.request import current_request
from mezzanine.blog.models import BlogPost
from .models import *

@processor_for('/')
def processor_home(request, page):
    highlights = sorted(chain(BlogPost.objects.filter(highlight=True),Boat.objects.filter(highlight=True)))
    # REPRENDRE (évincer les highlights déjà publiés au dessus)
    last_blogPosts = BlogPost.objects.filter()[:3]
    print "YAY -> %s" % last_blogPosts
    return locals()