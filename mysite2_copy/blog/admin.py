from django.contrib import admin
from blog.models import Post, Category,Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Post)
#class PostAdmin(admin.ModelAdmin):
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title',)
    # exclude = ('title',)
    list_display = ('title', 'counted_view', 'status', 'author', 'login_require', 'published_date', 'created_date')
    list_filter = ('status',)
    #ordering = ['created_date']
    search_fields = ['title','content']

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','post','approved', 'created_date')
    list_filter = ('post','approved')
    search_fields = ['name','post']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)