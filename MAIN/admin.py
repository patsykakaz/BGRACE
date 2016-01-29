
#-*- coding: utf-8 -*-

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import *

from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost



BoatAdmin_extra_fieldsets = (
    (None,
        {'fields': ('illustration','logo_boat','documentation','headline',
                    'presentation','architecte','longueur_HT',
                    'longueur_coque','largeur','tirant_eau','deplacement',
                    'leste','surface_voile','spi','motorisation',
                    'capacite_carburant','capacite_eau','cabines',
                    'certification_CE','association_classe'
                    )
        }
    ),
)

class BoatDocumentationInline(admin.TabularInline):
    model = BoatDocumentation

class BoatPalmaresInline(admin.TabularInline):
    model = BoatPalmares

class BoatAdmin(PageAdmin):
    inlines = (BoatDocumentationInline,BoatPalmaresInline)
    fieldsets = deepcopy(PageAdmin.fieldsets) + BoatAdmin_extra_fieldsets


admin.site.register(Boat, BoatAdmin)













