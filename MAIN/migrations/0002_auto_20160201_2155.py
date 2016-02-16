# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('MAIN', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Distributeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=255)),
                ('website', models.URLField()),
                ('mail', models.EmailField(max_length=254)),
                ('horaires', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Distributeur',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('illustration', models.ImageField(upload_to='/Users/patsykakaz_LSC/Documents/PRO/BGRACE/MAIN/static/media/distributeur/illustration')),
                ('logo', models.ImageField(upload_to='/Users/patsykakaz_LSC/Documents/PRO/BGRACE/MAIN/static/media/distributeur/logo_distributeur')),
                ('pays', django_countries.fields.CountryField(max_length=2)),
                ('bassin_navigation', models.CharField(blank=True, max_length=255, null=True)),
                ('presentation', mezzanine.core.fields.RichTextField(verbose_name='Presentation')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
        migrations.RenameField(
            model_name='boat',
            old_name='logo_boat',
            new_name='logo',
        ),
        migrations.AddField(
            model_name='contact_distributeur',
            name='Distributeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MAIN.Distributeur'),
        ),
    ]