# Generated by Django 4.2.5 on 2023-10-04 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cameras', '0002_alter_tarefas_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarefas',
            options={'ordering': ['id'], 'verbose_name': 'Tarefa', 'verbose_name_plural': 'Tarefas'},
        ),
    ]