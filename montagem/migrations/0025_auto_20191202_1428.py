# Generated by Django 2.2.7 on 2019-12-02 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('montagem', '0024_equipe_encontro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membros',
            name='equipe',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='montagem.Equipe'),
        ),
        migrations.AlterField(
            model_name='membros',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='montagem.Person'),
        ),
    ]
