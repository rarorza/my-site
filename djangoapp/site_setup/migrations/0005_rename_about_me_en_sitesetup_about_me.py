# Generated by Django 4.2.15 on 2024-08-11 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0004_alter_sitesetup_about_me_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitesetup',
            old_name='about_me_en',
            new_name='about_me',
        ),
    ]