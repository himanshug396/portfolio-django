# Generated by Django 3.1.4 on 2021-01-08 11:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hitman', '0005_auto_20210108_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutmeText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('full_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('use', models.BooleanField(default=False)),
            ],
        ),
    ]
