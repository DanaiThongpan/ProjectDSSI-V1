from django.db import models

# Create your models here.
class register_studens(models.Model):
    id_std = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    faculty = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.id_std} {self.username} {self.password}'