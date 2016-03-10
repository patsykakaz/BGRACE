#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate, get_backends
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMultiAlternatives

from mezzanine.utils.urls import login_redirect, next_url
from .models import *
from forms import *

def contact(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            source = request.POST['hiddenSource']
            if source == 'Contact':
                pass
            elif source == 'Boat':
                try: 
                    boatTarget = Boat.objects.get(id=int(request.POST['hiddenTarget']))
                except: 
                    boatTarget = 'Non spécifié / unknown'
            elif source == 'Distributeur':
                pass

            try:
                subject= 'TEST MAIL BG RACE'
                from_email = 'info@bgrace.fr'
                text_content = 'TEST BG RACE'
                html_content = 'Une demande de renseignement a été formulée depuis le site ARCHAMBAULT BY BG RACE <br /> concernant : <br />-  un bateau neuf <br />- '+ boatTarget +' IDENTITÉ : '+ request.POST['name'] +'  <br />MAIL : '+ request.POST['mail'] +' <br />TEL : '+ request.POST['phone'] +'<br /> MESSAGE : '+ request.POST['content']
                msg = EmailMultiAlternatives(subject, text_content, from_email, ['philippe@lesidecar.fr'])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                success = True
            except:
                success = False
                print "MAIL FAILED"

            return render(request, 'contact.html', locals())
        else:
            source = request.POST['hiddenSource']
            form = ContactForm(request)
            return render(request, 'contact.html', locals())
    else:
        form = ContactForm()



