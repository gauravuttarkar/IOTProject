# Generated by Django 2.1.7 on 2019-04-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='object',
            fields=[
                ('objectName', models.CharField(default=None, max_length=100)),
                ('objectID', models.CharField(default=None, max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(default='', max_length=100, null=True)),
                ('image', models.CharField(default=None, max_length=300)),
            ],
        ),
    ]
