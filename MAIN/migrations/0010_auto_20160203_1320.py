# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 13:20
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0009_auto_20160203_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='logo',
            field=mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Logo'),
        ),
    ]
