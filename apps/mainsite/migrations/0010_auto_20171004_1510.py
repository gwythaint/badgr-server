# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-04 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0009_applicationinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationinfo',
            name='allowed_scopes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='applicationinfo',
            name='website_url',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='applicationinfo',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='applicationinfo',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=254, null=True),
        ),
    ]
