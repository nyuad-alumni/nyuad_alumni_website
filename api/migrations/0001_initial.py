# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('region', models.CharField(max_length=60)),
                ('latitude', models.CharField(max_length=60)),
                ('longitude', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PreProfessionalTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudyAbroadSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_id', models.CharField(max_length=12)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('graduation_year', models.CharField(max_length=4)),
                ('preferred_email', models.CharField(max_length=40)),
                ('social_networks', models.CharField(max_length=400, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.City')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Company')),
                ('majors', models.ManyToManyField(to='api.Major')),
                ('preprofessional_tracks', models.ManyToManyField(to='api.PreProfessionalTrack')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.School')),
                ('study_abroads', models.ManyToManyField(to='api.StudyAbroadSite')),
            ],
        ),
    ]
