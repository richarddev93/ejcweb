# Generated by Django 2.2.7 on 2019-11-21 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('montagem', '0016_auto_20191120_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dt_nasc',
            field=models.DateField(blank=True, null=True),
        ),
    ]
