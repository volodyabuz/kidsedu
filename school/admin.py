from django.contrib import admin
from .models import *


class EducationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'about', 'type_edu')
    list_display_links = ('id', 'name', 'about')
    search_fields = ('name',)
    list_editable = ('type_edu',)
    list_filter = ('min_age_kids',)
    prepopulated_fields = {'slug': ('name',)}


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name',)
    list_display_links = ('type_name',)
    prepopulated_fields = {'slug': ('type_name',)}

class PhotoEducationAdmin(admin.ModelAdmin):
    list_display = ('name_edu', 'photo')
    prepopulated_fields = {'slug': ('name_edu',)}

admin.site.register(Educations, EducationsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(PhotoEducations, PhotoEducationAdmin)
