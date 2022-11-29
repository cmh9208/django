# Generated by Django 4.1.3 on 2022-11-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buser',
            fields=[
                ('id', models.IntegerField(auto_created=True, max_length=30, primary_key=True, serialize=False)),
                ('email', models.TextField()),
                ('nickname', models.TextField()),
                ('password', models.TextField()),
            ],
            options={
                'db_table': 'buser',
            },
        ),
    ]
