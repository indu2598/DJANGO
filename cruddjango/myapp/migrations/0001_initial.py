# Generated by Django 3.1.3 on 2020-11-15 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('authorname', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
    ]
