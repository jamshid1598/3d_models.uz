# Generated by Django 3.1.1 on 2021-03-04 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='video_file',
        ),
        migrations.RemoveField(
            model_name='product',
            name='video_link',
        ),
    ]
