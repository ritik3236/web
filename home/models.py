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
        return str(self.sub_names)


class QuesPaper(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.IntegerField(unique=True)
    sub_name = models.CharField(max_length=20)
    fl_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.course_name} {self.semester}sem {self.sub_name}"
