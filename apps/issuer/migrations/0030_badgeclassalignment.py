# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-14 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0029_badgeinstance_recipient_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='BadgeClassAlignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_json', models.TextField(blank=True, default=None, null=True)),
                ('target_name', models.TextField()),
                ('target_url', models.CharField(max_length=2083)),
                ('target_description', models.TextField(blank=True, default=None, null=True)),
                ('target_framework', models.TextField(blank=True, default=None, null=True)),
                ('target_code', models.TextField(blank=True, default=None, null=True)),
                ('badgeclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issuer.BadgeClass')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
