# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 05:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firstmenus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('iconclass', models.CharField(blank=True, max_length=80)),
                ('comment', models.CharField(blank=True, max_length=160, null=True)),
            ],
            options={
                'db_table': 'meteor_firstmenus',
            },
        ),
        migrations.CreateModel(
            name='Secondmenus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('url', models.CharField(max_length=200)),
                ('onshow', models.BooleanField(default=False)),
                ('comment', models.CharField(blank=True, max_length=160, null=True)),
                ('firstmenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuManage.Firstmenus')),
            ],
            options={
                'db_table': 'meteor_secondmenus',
            },
        ),
    ]
