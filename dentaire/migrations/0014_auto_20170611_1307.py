# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentaire', '0013_ordonnance_observation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichepatient',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rdv',
            name='num_rdv',
            field=models.IntegerField(default='1'),
        ),
    ]
