# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LanguageExchange', '0003_myuser_status_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]