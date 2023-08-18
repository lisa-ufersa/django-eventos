# Generated by Django 4.2.3 on 2023-08-16 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voluntario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.evento')),
            ],
        ),
        migrations.CreateModel(
            name='Patrocinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cnpj', models.CharField(max_length=100)),
                ('eventos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.evento')),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequencias', models.CharField(max_length=200)),
                ('certificado', models.ManyToManyField(to='eventos.certificado')),
            ],
        ),
        migrations.CreateModel(
            name='Ministrante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minieventos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.minievento')),
            ],
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.evento')),
            ],
        ),
    ]
