from django.contrib import admin

from models import Template


class TemplateAdmin(admin.ModelAdmin):
    fields = ['path', 'description', 'content']

admin.site.register(Template, TemplateAdmin)
