# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 07:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gad1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professor',
            old_name='department',
            new_name='dept',
        ),
        migrations.RenameField(
            model_name='professor',
            old_name='mobileno',
            new_name='m_no',
        ),
        migrations.RenameField(
            model_name='professor',
            old_name='name',
            new_name='pro_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='mobileno',
            new_name='m_no',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='student_name',
        ),
    ]
