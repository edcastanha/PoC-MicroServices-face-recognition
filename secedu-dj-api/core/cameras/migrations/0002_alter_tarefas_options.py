# Generated by Django 4.2.5 on 2023-10-03 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cameras', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarefas',
            options={'ordering': ['escalas'], 'verbose_name': 'Tarefa', 'verbose_name_plural': 'Tarefas'},
        ),
    ]
