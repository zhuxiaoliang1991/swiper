# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-06-16 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dating_sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], default='女', max_length=8, verbose_name='匹配性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_day',
            field=models.IntegerField(default=1, verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_month',
            field=models.IntegerField(default=1, verbose_name='出生月份'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_year',
            field=models.IntegerField(default=2000, verbose_name='出生年份'),
        ),
    ]
