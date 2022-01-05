from django.contrib import admin
from .models import Post, Comment


# Register your models here.

class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_date')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        CommentsInline,
    ]


admin.site.register(Post, PostAdmin)
