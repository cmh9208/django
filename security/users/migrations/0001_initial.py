# Generated by Django 4.1.4 on 2022-12-14 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.TextField()),
                ('password', models.CharField(max_length=10)),
                ('user_name', models.TextField()),
                ('phone', models.TextField()),
                ('birth', models.TextField()),
                ('address', models.TextField(blank=True)),
                ('job', models.TextField()),
                ('user_interests', models.TextField()),
                ('token', models.TextField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'users',
            },
        ),
    ]