# Generated by Django 2.2 on 2019-05-03 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vista', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticiasmodelo',
            old_name='subtitulo',
            new_name='resumen',
        ),
    ]
