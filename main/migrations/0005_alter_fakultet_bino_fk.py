# Generated by Django 5.1.4 on 2024-12-14 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_fakultet_yonalish_fakultet_yonalish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakultet',
            name='bino_fk',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.bino'),
        ),
    ]
