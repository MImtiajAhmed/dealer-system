from ctypes import Union
from typing import Tuple
from django.contrib import admin
from .models import Team
# from django.utils.html import format_html
# not working thumbnail
# not working thumbnail
    # def thumbnail(self, objects):
    #     return format_html('< img src="{}" width = "40" >'.format(objects.photo.url))
    
    # thumbnail.short_description = 'Photo'
    # not working thumbnail
    

class TeamAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'first_name', 'last_name', 'designation', 'created_date')
    list_display_links = ('first_name', )
    search_fields = ('first_name', 'designation')
    list_filter= ('designation',)
# Register your models here.
admin.site.register(Team, TeamAdmin)