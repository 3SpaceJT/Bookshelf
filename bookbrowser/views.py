from django.shortcuts import render
from django.views.generic import ListView, CreateView
from bookbrowser.models import Book


class BookList(ListView):
    context_object_name = 'book_list'
    # queryset = Book.objects.filter(publisher__name='ACME Publishing')
    # template_name = 'books/acme_list.html'


class NewBook(CreateView):
    pass
