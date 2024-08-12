# Generated by Django 4.2.15 on 2024-08-10 23:23

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import utils.models_validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('description', models.CharField(max_length=255)),
                ('show_header', models.BooleanField(default=True)),
                ('show_search', models.BooleanField(default=True)),
                ('show_menu', models.BooleanField(default=True)),
                ('show_description', models.BooleanField(default=True)),
                ('show_pagination', models.BooleanField(default=True)),
                ('show_footer', models.BooleanField(default=True)),
                ('about_me_pt', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=255), default=list, size=None)),
                ('about_me_en', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=255), default=list, size=None)),
                ('code_languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=255), default=list, size=None)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('favicon', models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m/', validators=[utils.models_validators.validate_png])),
                ('profile_pic', models.ImageField(blank=True, default='', upload_to='assets/profile_pic/%Y/%m/', validators=[utils.models_validators.validate_png])),
                ('cv', models.FileField(blank=True, default='', upload_to='assets/cv/%Y/%m/', validators=[utils.models_validators.validate_pdf])),
            ],
            options={
                'verbose_name': 'Setup',
                'verbose_name_plural': 'Setup',
            },
        ),
        migrations.CreateModel(
            name='MenuLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url_or_path', models.CharField(max_length=2048)),
                ('new_tab', models.BooleanField(default=False)),
                ('site_setup', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='site_setup.sitesetup')),
            ],
            options={
                'verbose_name': 'Menu Link',
                'verbose_name_plural': 'Menu Links',
            },
        ),
    ]
