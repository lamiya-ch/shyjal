# Generated by Django 5.0.6 on 2024-06-10 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='discription',
            new_name='description',
        ),
    ]
