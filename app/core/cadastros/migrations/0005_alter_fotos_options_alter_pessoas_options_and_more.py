# Generated by Django 4.2.4 on 2023-08-31 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_fotos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fotos',
            options={'verbose_name': 'Foto', 'verbose_name_plural': 'Fotos'},
        ),
        migrations.AlterModelOptions(
            name='pessoas',
            options={'verbose_name': 'Pessoa', 'verbose_name_plural': 'Pessoas'},
        ),
        migrations.RenameField(
            model_name='fotos',
            old_name='foto1',
            new_name='foto',
        ),
        migrations.RemoveField(
            model_name='fotos',
            name='foto2',
        ),
        migrations.RemoveField(
            model_name='fotos',
            name='foto3',
        ),
    ]