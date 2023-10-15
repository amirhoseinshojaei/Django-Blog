from django.contrib import admin
from .models import Blog,Comment
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    inlines = ['CommentInLine']
    list_display = ['title','author','pub_date']
    list_filter = ['author']
    search_fields = ['title']
    ordering = ['pub_date']
    date_hierarchy = "pub_date"

admin.site.register(Blog,BlogAdmin)

class CommentInLine(admin.TabularInline):
    model = Comment

admin.site.register(Comment)