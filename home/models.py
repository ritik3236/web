from django.db import models


# Create your models here.

class Course(models.Model):
    c_name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{str(self.id)} {self.c_name }"
