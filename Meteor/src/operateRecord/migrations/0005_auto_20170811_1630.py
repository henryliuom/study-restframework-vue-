# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operateRecord', '0004_auto_20170811_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='operaterecords',
            name='userip',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='operaterecords',
            name='date',
            field=models.DateTimeField(default=b'2017-08-11 16:30:32', verbose_name='\u64cd\u4f5c\u65f6\u95f4'),
        ),
    ]