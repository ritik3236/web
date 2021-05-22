import os

from django.conf import settings
from django.db import models

# Create your models here.


class Course(models.Model):
    c_name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.c_name


class Subject(models.Model):
    course_name = models.OneToOneField(Course, on_delete=models.CASCADE)
    sub_names = models.TextField(max_length=50)

    def __str__(self):
        return f"{self.course_name} {self.sub_names}"


class QuesPaper(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.IntegerField()
    sub_name = models.CharField(max_length=20)
    fl_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_name} {self.semester}Sem {self.sub_name}"


class QuesPaperMedia(models.Model):
    file_name = models.CharField(max_length=50)
    file_date = models.DateField()
    q_paper = models.FileField(upload_to='q_paper')
    fl_id = models.CharField(max_length=30)
    def __str__(self):
        return self.file_name

    @property
    def relative_path(self):
        return os.path.relpath(self.path, settings.MEDIA_ROOT)
    
    def file_size(self):
        x = self.q_paper.size
        y = 512000
        if x < y:
            value = round(x/1000, 1)
            ext = ' KB'
        else:
            value = round(x/1000000, 1)
            ext = ' MB'
        return str(value)+ext
