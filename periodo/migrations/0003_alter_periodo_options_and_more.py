# Generated by Django 4.1.4 on 2023-01-23 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('periodo', '0002_alter_periodo_fecha_termino'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='periodo',
            options={'ordering': ['-fecha_inicio'], 'verbose_name': 'periodo', 'verbose_name_plural': 'periodos'},
        ),
        migrations.RenameField(
            model_name='periodo',
            old_name='fecha_inicio_periodo',
            new_name='fecha_inicio',
        ),
    ]
