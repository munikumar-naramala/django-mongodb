# Generated by Django 4.1.7 on 2023-03-03 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_parser_mongo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logparsermongo',
            name='device',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='logparsermongo',
            name='vendor',
            field=models.CharField(max_length=100),
        ),
    ]
