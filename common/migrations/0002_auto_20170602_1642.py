# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-02 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='web_link',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='common.WebLink'),
            preserve_default=False,
        ),
    ]
