# Generated by Django 2.0 on 2018-05-30 16:51

from django.db import migrations, models
import ourblog.models


class Migration(migrations.Migration):

    dependencies = [
        ('ourblog', '0005_auto_20180530_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='profile_image',
            field=models.FileField(blank=True, upload_to=ourblog.models.profile_image),
        ),
    ]
