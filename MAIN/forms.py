#-*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives

class ContactForm(forms.Form):
    name = forms.CharField(label='Identité/Identity')
    mail = forms.CharField(label='Email/Mail', widget=forms.EmailInput)
    phone = forms.CharField(label='Téléphone/Phone')
    content = forms.TextField(label='Message')