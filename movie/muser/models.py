from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Muser(models.Model):
    use_in_migration = True
    id = models.IntegerField(primary_key=True, auto_created=True, max_length=30)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()
    age = models.TextField()

    class Meta:
        db_table = "muser"

    def __str__(self):
        return f'{self.pk} {self.email} {self.nickname} {self.password} {self.age}'



