# Generated by Django 4.1.3 on 2022-11-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopSuser',
            fields=[
                ('suer_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.TextField()),
                ('nickname', models.TextField()),
                ('password', models.TextField()),
                ('point', models.TextField()),
            ],
            options={
                'db_table': 'shop_susers',
            },
        ),
    ]
