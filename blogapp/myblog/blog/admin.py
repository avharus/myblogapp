from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "date")

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)
