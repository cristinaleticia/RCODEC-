# Generated by Django 4.0.5 on 2022-11-14 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcodec', '0007_rename_materia_repositorio_titulor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tcc',
            old_name='materia',
            new_name='descricao',
        ),
    ]