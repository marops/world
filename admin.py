from django.contrib.gis import admin
#from django.contrib import admin

from .models import WorldBorder, States, Tiles, Projects


from . import models

admin.site.site_header = 'Geodjango Tutorial'

class StatesAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering=['name']
    fields=['name','geom']
    #pass

class WorldAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering=['name']

class TileAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    search_fields = ['name']
    fields = ['name', 'note','geom']
    ordering=['name']

class ProjectsAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    search_fields = ['name']
    fields = ['name', 'geom']
    ordering=['name']

#admin.site.register(WorldBorder)
admin.site.register(States, StatesAdmin)
admin.site.register(WorldBorder, WorldAdmin)
admin.site.register(Tiles, TileAdmin)
admin.site.register(Projects, ProjectsAdmin)
#admin.site.register(WorldBorder, admin.OSMGeoAdmin,list_display=('name',))