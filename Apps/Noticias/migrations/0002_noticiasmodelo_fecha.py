# Generated by Django 2.2 on 2019-05-02 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Noticias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticiasmodelo',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
