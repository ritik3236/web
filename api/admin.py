from django.contrib import admin

# Register your models here.
from api.models import *


class QuotesApiAdmin(admin.ModelAdmin):
    list_display = ('author', 'sort_quote', 'source', 'uploaded_at')
    list_display_links = ('author', 'sort_quote')


class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'uploaded_at', 'description')


admin.site.register(QuotesApi, QuotesApiAdmin)
admin.site.register(FileUpload, FileUploadAdmin)
