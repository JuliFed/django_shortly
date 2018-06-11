# Generated by Django 2.0.6 on 2018-06-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortly',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(unique=True)),
                ('clicked', models.IntegerField(default=0)),
            ],
        ),
    ]
