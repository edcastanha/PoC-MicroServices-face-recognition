# Generated by Django 4.2.5 on 2023-11-08 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_alter_fotos_pessoa'),
        ('cameras', '0017_alter_faces_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequenciasescolar',
            name='aluno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastros.pessoas'),
        ),
    ]