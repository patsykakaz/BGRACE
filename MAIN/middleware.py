#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings

from MAIN.models import *


class ContentMiddleware(object):
    def process_template_response(self, request, response):
        distributeur = Distributeur.objects.all()
        response.context_data['Boats'] = Boat.objects.all()[:7]
        response.context_data['Distributeurs'] =Distributeur.objects.all()
        return response
