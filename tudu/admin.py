from django.contrib import admin

from tudu.models import Todo



@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "created_at")


    
