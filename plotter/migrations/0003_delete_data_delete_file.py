# Generated by Django 4.2 on 2023-04-13 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plotter', '0002_rename_datay_data_rename_filex_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]