# Generated by Django 4.2.15 on 2024-08-10 23:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetup',
            name='about_me_en',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=255), default=list, size=None), size=None),
        ),
        migrations.AlterField(
            model_name='sitesetup',
            name='about_me_pt',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=255), default=list, size=None), size=None),
        ),
        migrations.AlterField(
            model_name='sitesetup',
            name='code_languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=255), default=list, size=None), size=None),
        ),
    ]