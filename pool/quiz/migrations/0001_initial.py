# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-24 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='QuizName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quizName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.QuizName'),
        ),
    ]
