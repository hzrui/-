# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-24 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sup_uesr', '0003_auto_20180924_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='head',
            field=models.ImageField(default='user/201809/24/1.jpg', upload_to='head/%Y/%m', verbose_name='用户头像'),
        ),
    ]
