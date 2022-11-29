# Generated by Django 4.1.3 on 2022-11-29 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(auto_created=True, max_length=30, primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('created_at', models.TextField()),
                ('rank', models.IntegerField(default=1)),
                ('point', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]