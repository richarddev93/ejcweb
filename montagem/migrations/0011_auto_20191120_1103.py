# Generated by Django 2.2.7 on 2019-11-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('montagem', '0010_auto_20191118_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='profile_picture'),
        ),
    ]
