from blog.models import Post, Comment
from django.contrib import admin

admin.site.register(Comment)

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    inlines = [CommentInline]
    
admin.site.register(Post, PostAdmin)
