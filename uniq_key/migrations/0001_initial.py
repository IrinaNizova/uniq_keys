# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-19 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=4)),
                ('status', models.CharField(choices=[('N', 'not_issued'), ('I', 'issued'), ('R', 'repaid')], max_length=1)),
            ],
        ),
    ]
