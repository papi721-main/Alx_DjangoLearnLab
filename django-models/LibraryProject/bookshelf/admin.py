#!/usr/bin/env python3
from django.contrib import admin

from .models import Book


# Customize admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("title", "author", "publication_year")
    search_fields = ("title", "author")


# Register your models here.
admin.site.register(Book, BookAdmin)
