#-*- coding: utf-8 -*-

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import *

from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost



blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(-2, "highlight")
# blog_fieldsets[0][1]["fields"].insert(-2, "baseline")
class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets


BoatAdmin_extra_fieldsets = (
    (None,
        {'fields': ('highlight','featured_image',
                    'sidecut_image','sidecut_image_2',
                    'logo','baseline',
                    'occasion','price','annee_construction',
                    'presentation','architecte',
                    'longueur_HT',
                    'longueur_coque','largeur',
                    'tirant_eau','deplacement',
                    'lest','surface_voile','spi',
                    'motorisation','capacite_carburant',
                    'capacite_eau','cabines',
                    'certification_CE',
                    'association_classe'
                )
        }
    ),
)

class BoatGaleryInline(admin.TabularInline):
    model = BoatGalery

class BoatDocumentationInline(admin.TabularInline):
    model = BoatDocumentation

class BoatPalmaresInline(admin.TabularInline):
    model = BoatPalmares

class BoatAdmin(PageAdmin):
    inlines = (BoatGaleryInline, BoatDocumentationInline, BoatPalmaresInline)
    fieldsets = deepcopy(PageAdmin.fieldsets) + BoatAdmin_extra_fieldsets


DistributeurAdmin_extra_fieldsets = (
    (None,
        {'fields': ('illustration','logo','pays',
                    'bassin_navigation','presentation',
                    'nom','adresse','tel','website',
                    'mail','horaires',
                    )
        }
    ),
)

class BassinNavAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets)

class DistributeurAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + DistributeurAdmin_extra_fieldsets


admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)
admin.site.register(Boat, BoatAdmin)
admin.site.register(BassinNav, BassinNavAdmin)
admin.site.register(Distributeur, DistributeurAdmin)













