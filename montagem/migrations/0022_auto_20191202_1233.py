# Generated by Django 2.2.7 on 2019-12-02 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('montagem', '0021_equipe_ano'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='membs',
        ),
        migrations.AddField(
            model_name='equipe',
            name='membs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='montagem.Person'),
            preserve_default=False,
        ),
    ]
