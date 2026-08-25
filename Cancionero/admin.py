from django.contrib import admin
from .models import Cancion

class CancionAdmin(admin.ModelAdmin):
    list_display= ('id','titulo')
    
    list_display_links = ('id','titulo')
    
    search_fields = ('titulo',)
    
    ordering = ('titulo','id')
    

admin.site.register(Cancion,CancionAdmin)

# Register your models here.
