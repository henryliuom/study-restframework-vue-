# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyManage', '0009_auto_20170807_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dutysheets',
            name='date',
            field=models.DateTimeField(blank=True, default=b'2017-08-07 16:23:43', null=True, verbose_name='\u4ea4\u63a5\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='dutysheets',
            name='deleteDate',
            field=models.DateTimeField(blank=True, default=b'2017-08-07 16:23:43', null=True, verbose_name='\u5220\u9664\u65f6\u95f4'),
        ),
    ]
