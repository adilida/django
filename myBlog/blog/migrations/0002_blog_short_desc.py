# Generated by Django 4.1.6 on 2023-02-22 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_desc',
            field=models.CharField(default='', max_length=300),
        ),
    ]
