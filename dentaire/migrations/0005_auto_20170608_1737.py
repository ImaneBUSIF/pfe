# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentaire', '0004_auto_20170608_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='role',
            field=models.CharField(default='utilisateur', max_length=254),
        ),
    ]
