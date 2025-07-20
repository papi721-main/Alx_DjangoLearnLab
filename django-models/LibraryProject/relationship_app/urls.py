#!/usr/bin/env python3
from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/', views.LibraryListView.as_view(), name='library_list'),
]
