# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-08 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsisprod', '0002_auto_20160708_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='dataTermino',
            field=models.DateTimeField(null=True, verbose_name='Data de Término'),
        ),
    ]