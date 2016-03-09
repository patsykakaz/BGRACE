#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate, get_backends
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from mezzanine.utils.urls import login_redirect, next_url
from .models import *

def message(request):
    if request.POST:
        form = contactForm(request)
        if form.is_valid():
            pass
        else:
            source = request.POST['hiddenSource']
            form = contactForm(request)
            return render(request, 'contact.html', locals())
    else:
        form = contactForm()