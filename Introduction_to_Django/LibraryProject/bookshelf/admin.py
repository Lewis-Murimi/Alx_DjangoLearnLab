from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year')
    list_filter = ('title','author','published_year')

admin.site.register(Book)
