# Generated by Django 2.2.7 on 2019-12-02 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('montagem', '0023_auto_20191202_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='encontro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='montagem.Encontro'),
            preserve_default=False,
        ),
    ]
