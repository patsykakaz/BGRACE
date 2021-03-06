#-*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from .models import *
from mezzanine.core.translation import TranslatedDisplayable, TranslatedRichText
from mezzanine.blog.models import BlogCategory, BlogPost

class TranslatedBoat(TranslationOptions):
    fields = ('baseline','price','presentation','motorisation','certification_CE')

class TranslatedBoatGalery(TranslationOptions):
    fields = ('description',)

class TranslatedBoatDocumentation(TranslationOptions):
    fields = ('alternative_doc_nature',)

class TranslatedDistributeur(TranslationOptions):
    fields = ('pays','presentation','horaires')

class TranslatedBassinNav(TranslationOptions):
    fields = ()


# class TranslatedBlogPost(TranslatedDisplayable, TranslatedRichText):
    # fields = ('baseline',)


# translator.unregister(BlogPost)
# translator.register(BlogPost, TranslatedBlogPost)

translator.register(Boat, TranslatedBoat)
translator.register(BoatGalery, TranslatedBoatGalery)
translator.register(BoatDocumentation, TranslatedBoatDocumentation)
translator.register(Distributeur, TranslatedDistributeur)
translator.register(BassinNav, TranslatedBassinNav)