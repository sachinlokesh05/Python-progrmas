# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-20 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
