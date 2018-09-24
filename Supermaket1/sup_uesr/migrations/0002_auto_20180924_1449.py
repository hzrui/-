# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-24 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sup_uesr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.ImageField(upload_to='user/%Y%m/%d', verbose_name='用户的头像')),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='head',
            field=models.ImageField(default='default/infortx.png', upload_to='head/%Y/%m', verbose_name='用户头像'),
        ),
    ]
