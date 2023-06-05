from django.contrib import admin
from .models import PostModel, Category, Contact
# Register your models here.

@admin.register(PostModel)
class AdminPost(admin.ModelAdmin):
    list_display = ['id','title', 'slug','image',
                    'author', 'created_time','category',
                    'status']
    search_fields = ['title', 'author']
    list_filter = ['status', 'category', 'author']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_time'
    ordering = ['-published_time', 'status']
# @admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'id']

admin.site.register(Category, AdminCategory)
admin.site.register(Contact)