from django.contrib import admin

from home.models import *


# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ['id']


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'sub_names')


class QuesPaperAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'semester', 'sub_name', 'fl_name',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(QuesPaper, QuesPaperAdmin)
# admin.site.register(Semester)
