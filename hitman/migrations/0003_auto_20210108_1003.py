# Generated by Django 3.1.4 on 2021-01-08 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hitman', '0002_project_company_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationitem',
            name='url',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='quoteme',
            name='name',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
