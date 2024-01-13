# Generated by Django 4.2.5 on 2023-11-06 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastros', '0005_alter_fotos_pessoa'),
        ('cameras', '0014_delete_faceverify'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagensTratadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('auditado', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('face', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cameras.faces')),
            ],
            options={
                'verbose_name': 'Imagem Tratada',
                'verbose_name_plural': 'Imagens Tratadas',
                'ordering': ['id', 'auditado', 'status'],
            },
        ),
        migrations.CreateModel(
            name='FacesVerify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('verify', models.BooleanField(default=False)),
                ('distance', models.FloatField(default=0.0)),
                ('auditado', models.BooleanField(default=False)),
                ('face', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cameras.faces')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.pessoas')),
            ],
            options={
                'verbose_name': 'Face Auditada',
                'verbose_name_plural': 'FAces Auditadas',
            },
        ),
        migrations.CreateModel(
            name='FacesPrevisaoEmocional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('auditado', models.BooleanField(default=False)),
                ('predominante', models.CharField(choices=[('angry', 'Zangada'), ('disgust', 'Repulsa'), ('fear', 'Medo'), ('happy', 'Feliz'), ('neutral', 'Neutra'), ('sad', 'Triste'), ('surprise', 'Surpresa')], default='neutral', max_length=10)),
                ('zangado', models.FloatField(default=0.0)),
                ('repulsa', models.FloatField(default=0.0)),
                ('medo', models.FloatField(default=0.0)),
                ('feliz', models.FloatField(default=0.0)),
                ('neutro', models.FloatField(default=0.0)),
                ('triste', models.FloatField(default=0.0)),
                ('surpresa', models.FloatField(default=0.0)),
                ('region', models.CharField(blank=True, max_length=100)),
                ('face', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cameras.faces')),
                ('pessoa', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cadastros.pessoas')),
            ],
            options={
                'verbose_name': 'Face Previsão Emocional',
                'verbose_name_plural': 'Faces Previsão Emocional',
                'ordering': ['id', 'auditado'],
            },
        ),
    ]