# Generated by Django 4.2.5 on 2023-09-04 20:11

import core.cadastros.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contratos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('protocolo', models.CharField(max_length=100)),
                ('assinado_em', models.DateTimeField()),
                ('responsavel', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Contrato',
                'verbose_name_plural': 'Contratos',
            },
        ),
        migrations.CreateModel(
            name='Escolas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.contratos')),
            ],
            options={
                'verbose_name': 'Escola',
                'verbose_name_plural': 'Escolas',
            },
        ),
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], max_length=1)),
                ('perfil', models.CharField(choices=[('T', 'Tutor'), ('C', 'Colaborador'), ('E', 'Estudante')], max_length=1)),
                ('ra', models.CharField(blank=True, max_length=10, null=True)),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.escolas')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to=core.cadastros.models.Fotos.get_upload_path)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.pessoas')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
            },
        ),
    ]
