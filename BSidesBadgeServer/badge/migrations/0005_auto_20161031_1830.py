# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-31 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badge', '0004_auto_20161031_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='badge_challenges',
            field=models.ManyToManyField(blank=True, null=True, to='badge.Challenges'),
        ),
    ]
