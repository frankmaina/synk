# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-18 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("data", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="images",
            name="has_been_set",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="images",
            name="user_likes",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="images", name="web_likes", field=models.IntegerField(default=0)
        ),
    ]
