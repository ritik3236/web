from django.contrib import admin

from home.models import *


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ['id']


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'sub_names')


class QuesPaperAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'semester', 'sub_name', 'fl_id',)
    list_display_links = ('course_name', 'fl_id')


class QuesPaperMediaAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'fl_id', 'file_size')

class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'uploaded_at', 'description')


admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(QuesPaper, QuesPaperAdmin)
admin.site.register(FileUpload, FileUploadAdmin)
admin.site.register(QuesPaperMedia, QuesPaperMediaAdmin)
