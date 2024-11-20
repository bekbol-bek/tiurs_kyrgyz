# Generated by Django 5.1 on 2024-08-20 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_ecosystemtype_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ecocistem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ecosystemtype')),
            ],
        ),
    ]
