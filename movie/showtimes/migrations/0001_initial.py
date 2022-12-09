# Generated by Django 4.1.3 on 2022-11-30 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        ('theaters', '0001_initial'),
        ('cinemas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieShowtime',
            fields=[
                ('showtime_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('movie_cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemas.moviecinema')),
                ('movie_movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('movie_theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theaters.movietheater')),
            ],
            options={
                'db_table': 'movie_showtimes',
            },
        ),
    ]