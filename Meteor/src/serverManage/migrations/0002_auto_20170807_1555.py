# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverManage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='expiredate',
            field=models.DateTimeField(blank=True, default=b'2017-08-07 15:55:39', null=True, verbose_name='\u8fc7\u671f\u65f6\u95f4'),
        ),
    ]