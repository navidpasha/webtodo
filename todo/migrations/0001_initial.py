# Generated by Django 4.2.7 on 2023-11-25 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
