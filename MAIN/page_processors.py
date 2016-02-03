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
    # for element in highlights:
        # if 'boat' in element.featured_image.name:
            # illustration = element.featured_image.name.split('/')
            # element.featured_image = illustration[-1]
    print 'highlights = %s' % highlights
    return locals()