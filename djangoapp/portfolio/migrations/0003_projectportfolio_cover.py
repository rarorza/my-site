# Generated by Django 4.2.6 on 2023-10-16 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_project_projectportfolio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectportfolio',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='projects/%Y/%m'),
        ),
    ]
