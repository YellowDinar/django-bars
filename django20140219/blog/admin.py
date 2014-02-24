from django.contrib import admin
from blog.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'text', 'date')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)