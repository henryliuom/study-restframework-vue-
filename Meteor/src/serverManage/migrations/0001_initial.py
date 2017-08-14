# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 05:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userPermission', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idcs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('location', models.CharField(max_length=128, verbose_name='\u5730\u5740')),
                ('telephone', models.CharField(max_length=128, verbose_name='\u7535\u8bdd')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userPermission.Staffs', verbose_name='\u673a\u623f\u8d1f\u8d23\u4eba')),
            ],
            options={
                'db_table': 'classmate_idcs',
                'verbose_name': '\u673a\u623f',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userPermission.Staffs', verbose_name='\u9879\u76ee\u8d1f\u8d23\u4eba')),
            ],
            options={
                'db_table': 'classmate_projects',
                'verbose_name': '\u9879\u76ee',
            },
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u670d\u52a1\u5668\u540d\u79f0')),
                ('sn', models.CharField(blank=True, max_length=32, null=True, verbose_name='')),
                ('cpu', models.CharField(blank=True, max_length=64, null=True, verbose_name='')),
                ('mem', models.IntegerField(blank=True, null=True, verbose_name='\u5185\u5b58')),
                ('disktype', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u78c1\u76d8\u7c7b\u578b')),
                ('diskcapacity', models.IntegerField(blank=True, null=True, verbose_name='\u78c1\u76d8\u5bb9\u91cf')),
                ('nic', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u7f51\u5361')),
                ('expiredate', models.DateTimeField(blank=True, default=b'2017-08-02 13:29:00', null=True, verbose_name='\u8fc7\u671f\u65f6\u95f4')),
                ('privateip', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u5185\u7f51IP')),
                ('publicip', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u516c\u7f51IP')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
                ('idc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serverManage.Idcs', verbose_name='\u6240\u5c5e\u673a\u623f')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userPermission.Staffs', verbose_name='\u670d\u52a1\u5668\u8d1f\u8d23\u4eba')),
            ],
            options={
                'db_table': 'classmate_servers',
                'verbose_name': '\u670d\u52a1\u5668',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u670d\u52a1\u540d\u79f0')),
                ('tags', models.CharField(blank=True, max_length=64, null=True, verbose_name='')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serverManage.Projects', verbose_name='\u6240\u5c5e\u9879\u76ee')),
            ],
            options={
                'db_table': 'classmate_services',
                'verbose_name': '\u670d\u52a1',
            },
        ),
    ]
