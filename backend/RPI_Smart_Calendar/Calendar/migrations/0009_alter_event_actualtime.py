# Generated by Django 3.2.5 on 2021-08-14 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calendar', '0008_auto_20210811_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='actualTime',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
