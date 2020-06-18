# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-06-18 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200616_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vip_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], max_length=8, verbose_name='性别'),
        ),
    ]