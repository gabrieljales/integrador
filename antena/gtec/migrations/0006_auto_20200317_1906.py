# Generated by Django 2.2.3 on 2020-03-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('gtec', '0005_clientes_reserva_vaga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='hora_dev',
            field=models.DateField(blank=True, null=True, verbose_name='Hora Devolução'),
        ),
    ]