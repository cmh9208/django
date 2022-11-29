from django.db import models

# Create your models here.

class User(models.Model):
    use_in_migration = True
    id = models.IntegerField(primary_key=True, auto_created=True, max_length=30)
    username = models.TextField()
    password = models.TextField()
    created_at = models.TextField()
    rank = models.IntegerField(default=1)
    point = models.IntegerField(default=0)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'{self.pk} {self.username} {self.password} {self.created_at} {self.rank} {self.point}'


