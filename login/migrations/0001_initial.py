# Generated by Django 2.0.3 on 2018-04-05 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tuser',
            fields=[
                ('user_id', models.CharField(max_length=30, primary_key='true', serialize=False)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('mobileno', models.CharField(max_length=30)),
                ('birthdate', models.DateTimeField()),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
