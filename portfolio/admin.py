from django.contrib import admin
from .models import Project

# Register your models here.
# Para mostrar los datos ocultos created y updated
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Project, ProjectAdmin)