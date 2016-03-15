#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
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
                try:
                    subject= 'Demande Contact via site Web'
                    from_email = settings.MAIL_SENDER
                    text_content = 'TEST BG RACE'
                    html_content = '<p> Une demande de renseignement a été formulée depuis le site ARCHAMBAULT BY BG RACE depuis la page <b> CONTACT</b> <br /> Sujet -> <b> '+ request.POST['sujet'] +'</b> </p> <b> <br /> INFORMATIONS CLIENT </b> <b>IDENTITÉ</b> : '+ request.POST['name'] +'  <br /> <b>MAIL</b> : '+ request.POST['mail'] +' <br /> <b>TEL</b> : '+ request.POST['phone'] +'<br /> <b>MESSAGE</b> : '+ request.POST['content']
                    msg = EmailMultiAlternatives(subject, text_content, from_email, [settings.MAIL_RECIPIENT])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                    success = True
                except:
                    error = True
            elif source == 'Distributeur':
                try: 
                    distribTarget = Distributeur.objects.get(id=int(request.POST['hiddenTarget']))
                except: 
                    distribTarget = 'Non spécifié / unknown'
                    error = True
                print distribTarget
                try:
                    subject= 'DEMANDE D\'INFOS DEPUIS ARCHAMBAULT by BG RACE'
                    from_email = settings.MAIL_SENDER
                    text_content = 'TEST BG RACE'
                    html_content_FR = "<u> English version below </u> <p>Bonjour,</p> <p>Une demande de renseignement a été formulée depuis le site internet ARCHAMBAULT BY BG RACE via votre page de distributeur officiel de nos bateaux. </p> <p>Voici le contenu de la demande : </p> <p><b>IDENTITÉ </b>:"+ request.POST['name'] +"</p> <p> <b>MAIL </b>: "+ request.POST['mail'] +"</p> <p><b>TEL</b> :"+ request.POST['phone'] +"</p> <p><b>SUJET</b> : " + request.POST['sujet'] + "</p> <p> <b>MESSAGE</b> : "+ request.POST['content'] +"</p> <p>Au cas où vous ne pourriez pas répondre à cette demande, nous vous prions de contacter : <br /> Louis Burton ou Servane Escoffier <br /> Mail : info@bgrace <br /> Tel: +33(0)2 23 15 14 92 </p> <p> Merci, <br /><h4>L'équipe Archambault by BG RACE</h4>"
                    html_content_EN = "<p> <b>ENGLISH VERSION</b> </p><p>Dear Sir, Dear Madam, </p> <p> A customer has requested informations through your dedicated page on our Website. </p> <p> The following states the request : </p> <p> <b>NAME </b>:"+ request.POST['name'] +"</p> <p> <b>MAIL </b>: "+ request.POST['mail'] +"</p> <p><b>PHONE</b> : "+ request.POST['phone'] +"</p> <p> <b>SUBJECT: </b>" +request.POST['sujet']+ "</p> <p> <b>MESSAGE</b> : "+ request.POST['content'] +" </p> <p>Should it be impossible for you to answer the aformentioned, please contact : </p> <p>Servane ESCOFFIER or Louis BURTON <br /> Mail: info@bgrace.fr <br /> Phone number: +33 (0)2 23 15 14 92 <br /> Thank you, <br /> <h4>Archambault by BG Race’s team</h4> </p>"
                    html_content = html_content_FR + '<br /><br /> <br />' + html_content_EN
                    msg = EmailMultiAlternatives(subject, text_content, from_email, [settings.MAIL_RECIPIENT, distribTarget.mail])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                    success = True
                except:
                    error = True
            elif source == 'Boat':
                try: 
                    boatTarget = Boat.objects.get(id=int(request.POST['hiddenTarget']))
                except: 
                    boatTarget = 'Non spécifié / unknown'
                    error = True
                try:
                    subject= 'Demande information bateau via site Web'
                    from_email = settings.MAIL_SENDER
                    text_content = 'TEST BG RACE'
                    if boatTarget != 'Non spécifié / unknown':
                        if not boatTarget.occasion:
                            html_content = '<p> Une demande de renseignement a été formulée depuis le site ARCHAMBAULT BY BG RACE concernant  un <u>bateau neuf</u> de type -> <b>'+ boatTarget.title +' </b></p> <b> INFORMATIONS CLIENT </b> <b>IDENTITÉ</b> : '+ request.POST['name'] +'  <br /> <b>MAIL</b> : '+ request.POST['mail'] +' <br /> <b>TEL</b> : '+ request.POST['phone'] +'<br /> <b>MESSAGE</b> : '+ request.POST['content']
                        else:
                            html_content = '<p> Une demande de renseignement a été formulée depuis le site ARCHAMBAULT BY BG RACE concernant  un <u>bateau d\'occasion</u> de type -> <b>'+ boatTarget.title +' </b> </p> <b> INFORMATIONS CLIENT </b> <b>IDENTITÉ</b> : '+ request.POST['name'] +'  <br /> <b>MAIL</b> : '+ request.POST['mail'] +' <br /> <b>TEL</b> : '+ request.POST['phone'] +'<br /> <b>MESSAGE</b> : '+ request.POST['content']
                    else:
                        html_content = '<p> Une demande de renseignement a été formulée depuis le site ARCHAMBAULT BY BG RACE concernant  un bateau (de nature inconnue) -> '+ boatTarget.title +' </p> <b> INFORMATIONS CLIENT </b> <b>IDENTITÉ</b> : '+ request.POST['name'] +'  <br /> <b>MAIL</b> : '+ request.POST['mail'] +' <br /> <b>TEL</b> : '+ request.POST['phone'] +'<br /> <b>MESSAGE</b> : '+ request.POST['content']
                    msg = EmailMultiAlternatives(subject, text_content, from_email, [settings.MAIL_RECIPIENT])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                    success = True
                except:
                    error = True
            return render(request, 'pages/contact.html', locals())
        else:
            print "form is not valid"
            source = request.POST['hiddenSource']
            if 'hiddenTarget' in request.POST: 
                target = request.POST['hiddenTarget']
            form = ContactForm(request)
            return render(request, 'pages/contact.html', locals())
    else:
        form = ContactForm()
        return render(request, 'pages/contact.html', locals())



