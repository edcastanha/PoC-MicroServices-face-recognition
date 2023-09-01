# Generated by Django 4.1.9 on 2023-06-08 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cameras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escolas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=14)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], max_length=1)),
                ('perfil', models.CharField(choices=[('T', 'Tutor'), ('C', 'Colaborador'), ('E', 'Estudante')], max_length=1)),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.escolas')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Presencas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cameras.locais')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.pessoas')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]