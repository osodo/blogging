# Generated by Django 2.0 on 2018-05-31 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourblog', '0006_auto_20180530_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(null=True, verbose_name='Date published'),
        ),
    ]
