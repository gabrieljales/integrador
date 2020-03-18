# Generated by Django 2.2.3 on 2019-07-24 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gtec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('active', 'Ativo'), ('draft', 'Rascunho')], max_length=15),
        ),
    ]