# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 18:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dentaire', '0010_auto_20170610_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rdv',
            name='id_secretaire',
            field=models.ForeignKey(default='3', on_delete=django.db.models.deletion.CASCADE, related_name='rdv_sec', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rdv',
            name='num_rdv',
            field=models.IntegerField(default='1', max_length=254),
        ),
    ]
