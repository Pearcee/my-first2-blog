
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person, feed

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass

#admin.site.register(feed)
@admin.register(feed)
class FeedAdmin(ImportExportModelAdmin):
    pass