# Generated by Django 2.2.7 on 2019-11-10 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('montagem', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Servo', 'verbose_name_plural': 'Servos'},
        ),
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='nome',
        ),
    ]
