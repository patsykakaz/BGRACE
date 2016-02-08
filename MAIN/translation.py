#-*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from .models import *
from mezzanine.core.translation import TranslatedDisplayable, TranslatedRichText
from mezzanine.blog.models import BlogCategory, BlogPost

class TranslatedBoat(TranslationOptions):
    fields = ('baseline','presentation',)

class TranslatedDistributeur(TranslationOptions):
    fields = ('presentation',)


# class TranslatedBlogPost(TranslatedDisplayable, TranslatedRichText):
    # fields = ('baseline',)


# translator.unregister(BlogPost)
# translator.register(BlogPost, TranslatedBlogPost)

translator.register(Boat, TranslatedBoat)
translator.register(Distributeur, TranslatedDistributeur)