# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='measure',
            field=models.CharField(choices=[('g', 'г.'), ('l', 'л.'), ('taste', 'по вкусу'), ('piece', 'шт.')], default='taste', max_length=10, verbose_name='Мера'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='quantity',
            field=models.FloatField(null=True, verbose_name='Количество', blank=True),
        ),
    ]
