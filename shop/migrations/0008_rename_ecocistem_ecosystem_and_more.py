# Generated by Django 5.1 on 2024-08-20 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_ecocistem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ecocistem',
            new_name='Ecosystem',
        ),
        migrations.RenameModel(
            old_name='EcosystemType',
            new_name='EcosystemCategory',
        ),
    ]
