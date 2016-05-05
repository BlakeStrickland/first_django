# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 02:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0002_auto_20160504_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_id',
            field=models.IntegerField(default=datetime.datetime(2016, 5, 5, 2, 9, 0, 901509, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='movie_id',
            field=models.IntegerField(default=datetime.datetime(2016, 5, 5, 2, 9, 9, 157904, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='rating',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='user_id',
            field=models.IntegerField(default=datetime.datetime(2016, 5, 5, 2, 9, 16, 734097, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='zip_code',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=140, null=True),
        ),
    ]
