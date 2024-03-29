# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-05 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0004_poll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Candidate')),
            ],
        ),
        migrations.AlterField(
            model_name='poll',
            name='area',
            field=models.CharField(max_length=15),
        ),
        migrations.AddField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Poll'),
        ),
    ]
