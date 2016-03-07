#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings

from MAIN.models import *


class ContentMiddleware(object):
    def process_template_response(self, request, response):
        if request.get_full_path().split('/')[1] == 'en':
            response.context_data['frLink'] = request.get_full_path()[3:]
        else:
            response.context_data['enLink'] = '/en'+request.get_full_path()
        return response
