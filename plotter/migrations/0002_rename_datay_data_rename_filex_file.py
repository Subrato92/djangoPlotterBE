# Generated by Django 4.2 on 2023-04-13 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plotter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DataY',
            new_name='Data',
        ),
        migrations.RenameModel(
            old_name='FileX',
            new_name='File',
        ),
    ]
