# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverManage', '0004_auto_20170807_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='expiredate',
            field=models.DateTimeField(blank=True, default=b'2017-08-08 10:52:13', null=True, verbose_name='\u8fc7\u671f\u65f6\u95f4'),
        ),
    ]
