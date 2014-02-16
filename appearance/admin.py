from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from django.conf import settings

from models import Template, TemplateResource, Theme, ThemeResource

from django_ace import AceWidget
from import_export.admin import ImportExportModelAdmin
import reversion
from fack.models import Question, Topic
from import_export import resources



class ThemeAdmin(ImportExportModelAdmin):
    resource_class = ThemeResource

# admin.site.register(Theme, ThemeAdmin)


class TemplateAdmin(ImportExportModelAdmin, reversion.VersionAdmin):
    resource_class = TemplateResource
    save_as = True
    formats = settings.IMPORT_EXPORT_FORMATS

    list_display = ( 'path', 'description' ,'created_at', 'updated_at')
    search_fields = ('path', 'description')
    # exclude = ('theme',)
    list_filter = ('theme',)

    formfield_overrides = {
        models.TextField: {'widget': AceWidget(mode='html', width='750px', height='700px')},

    }
admin.site.register(Template, TemplateAdmin)



### Adding FACK related model tweaks here

class TopicResource(resources.ModelResource):

    class Meta:
        model = Topic

class TopicAdmin(ImportExportModelAdmin, reversion.VersionAdmin):
    resource_class = TopicResource
    formats = settings.IMPORT_EXPORT_FORMATS

    prepopulated_fields = {'slug':('name',)}

admin.site.unregister(Topic)
admin.site.register(Topic, TopicAdmin)


class QuestionResource(resources.ModelResource):

    class Meta:
        model = Question

class QuestionAdmin(ImportExportModelAdmin, reversion.VersionAdmin):
    resource_class = QuestionResource
    formats = settings.IMPORT_EXPORT_FORMATS

    list_display = ['text', 'sort_order', 'created_by', 'created_on',
                    'updated_by', 'updated_on', 'status']
    list_editable = ['sort_order', 'status']

    def save_model(self, request, obj, form, change):
        '''
        Update created-by / modified-by fields.

        The date fields are upadated at the model layer, but that's not got
        access to the user.
        '''
        # If the object's new update the created_by field.
        if not change:
            obj.created_by = request.user

        # Either way update the updated_by field.
        obj.updated_by = request.user

        # Let the superclass do the final saving.
        return super(QuestionAdmin, self).save_model(request, obj, form, change)

admin.site.unregister(Question)
admin.site.register(Question, QuestionAdmin)

