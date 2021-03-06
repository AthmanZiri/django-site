# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='Images/None/No-img.jpg', upload_to='porfolio/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
