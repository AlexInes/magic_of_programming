from django.contrib import admin
from projects.models import Project, Image, Category, Tool

# Register your models here.
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Tool)