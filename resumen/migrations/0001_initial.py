# Generated by Django 4.1.4 on 2022-12-07 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('periodo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resumen',
            fields=[
                ('anio', models.IntegerField(primary_key=True, serialize=False)),
                ('sentencias', models.DecimalField(decimal_places=0, max_digits=4)),
                ('itinerancias', models.DecimalField(decimal_places=0, max_digits=2)),
                ('convenios', models.DecimalField(decimal_places=0, max_digits=2)),
                ('asuntos_ingresados', models.DecimalField(decimal_places=0, max_digits=4)),
                ('archivados', models.DecimalField(decimal_places=0, max_digits=4)),
                ('fk_periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perdiodo', to='periodo.periodo')),
            ],
            options={
                'verbose_name': 'resumen',
                'verbose_name_plural': 'resumenes',
                'db_table': 'Resumen',
                'ordering': ['-anio'],
            },
        ),
    ]
