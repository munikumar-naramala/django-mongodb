# Generated by Django 4.1.7 on 2023-03-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogParserMongo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=100)),
                ('device', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
