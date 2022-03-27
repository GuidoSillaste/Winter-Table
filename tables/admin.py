from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Dessert


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """" doc string """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """" doc string """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """" doc string """
        queryset.update(approved=True)

@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    """" doc string """
    list_display = ('title', 'post', 'created_on')
    list_filter = ('created_on',)