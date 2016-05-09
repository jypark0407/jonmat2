# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CongressMember',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('party', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Eat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jonmat.CongressMember')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=200)),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='eat',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jonmat.Restaurant'),
        ),
    ]