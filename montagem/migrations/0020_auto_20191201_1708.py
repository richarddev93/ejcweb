# Generated by Django 2.2.7 on 2019-12-01 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('montagem', '0019_auto_20191201_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='nome',
        ),
        migrations.AddField(
            model_name='equipe',
            name='nome_equipe',
            field=models.CharField(choices=[('animacao', 'Animação'), ('espera', 'Espera'), ('canto', 'Canto'), ('compras', 'Compras'), ('cozinha', 'Cozinha'), ('circulo', 'Círculo'), ('co_gerais', 'Coord.Gerais'), ('dirigentes', 'Dirigentes'), ('espirit', 'Espiritualizador'), ('interc', 'Intercessão'), ('lanche', 'Lanche'), ('faxina', 'FaxinaeLimpeza'), ('sala', 'Sala'), ('secretaria', 'Secretaria'), ('transito', 'OrdemeTrânsito'), ('visitação', 'Visitação')], default=1, max_length=30, verbose_name='Equipes:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='membros',
            name='status_conv',
            field=models.CharField(choices=[('a', 'Aguardando Convite'), ('e', 'Convite Enviado'), ('r', 'Convite Recusado'), ('d', 'Desistiu'), ('a', 'Aceito'), ('s', 'Sem Retorno')], default='Aguardando Convite', max_length=1, verbose_name='Status:'),
        ),
    ]
