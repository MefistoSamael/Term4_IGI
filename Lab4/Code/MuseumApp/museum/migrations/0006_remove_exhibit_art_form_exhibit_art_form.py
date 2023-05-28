# Generated by Django 4.2.1 on 2023-05-28 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0005_remove_exhibit_art_form_exhibit_art_form'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibit',
            name='art_form',
        ),
        migrations.AddField(
            model_name='exhibit',
            name='art_form',
            field=models.ManyToManyField(to='museum.artform'),
        ),
    ]
