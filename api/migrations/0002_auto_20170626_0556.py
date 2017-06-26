# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 05:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='study_abroads',
            new_name='study_abroad_sites',
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='api.City'),
        ),
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='api.Company'),
        ),
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='api.School'),
        ),
    ]
