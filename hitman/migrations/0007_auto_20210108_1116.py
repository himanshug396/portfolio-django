# Generated by Django 3.1.4 on 2021-01-08 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hitman', '0006_aboutmetext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutmetext',
            old_name='full_description',
            new_name='text',
        ),
    ]