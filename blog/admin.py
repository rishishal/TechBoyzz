from django.contrib import admin
from .models import Category, Post
from django.views.decorators.csrf import csrf_exempt


# Register your models here.
# for configuration of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url', 'add_date')
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

    class Media:
        js = ('https://cdn.tiny.cloud/1/x4i9rhr6h600i3jl1u1cvo99ogbz4i588fxpqz77p19cgqr1/tinymce/6/tinymce.min.js',
              'js/script.js',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
