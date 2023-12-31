# Generated by Django 4.2.6 on 2023-10-19 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='is_published',
            field=models.BooleanField(default=False, help_text='This field will need to be checked for the page to be displayed'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover_in_post_content',
            field=models.BooleanField(default=True, help_text='If checked, will display the cover within the post content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False, help_text='This field will need to be checked for the post to be displayed'),
        ),
    ]
