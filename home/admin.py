from django.contrib import admin

from home.models import Course


# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ['id']


admin.site.register(Course, CourseAdmin)
