from django.contrib import admin

from home.models import *


# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ['id']


admin.site.register(Course, CourseAdmin)
admin.site.register(Subject)
admin.site.register(QuesPaper)
# admin.site.register(Semester)
