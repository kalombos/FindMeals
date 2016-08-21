# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Название ингредиента', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recipie',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Название рецепта', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('quantity', models.FloatField(verbose_name='Количество')),
                ('measure', models.CharField(default='taste', verbose_name='Мера', choices=[('g', 'г'), ('л', 'л'), ('taste', 'по вкусу')], max_length=10)),
                ('ingredient', models.ForeignKey(to='searcher.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='recipie',
            name='variations',
            field=models.ManyToManyField(to='searcher.Variation'),
        ),
    ]
