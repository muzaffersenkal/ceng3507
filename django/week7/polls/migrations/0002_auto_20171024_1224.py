# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-24 12:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='votes',
            new_name='choice_votes',
        ),
    ]
