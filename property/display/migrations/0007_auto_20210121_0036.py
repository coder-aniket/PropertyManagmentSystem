# Generated by Django 3.1.5 on 2021-01-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0006_property_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='location',
        ),
        migrations.AddField(
            model_name='property',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='lng',
            field=models.FloatField(null=True),
        ),
    ]
