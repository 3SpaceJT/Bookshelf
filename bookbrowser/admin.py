from django.contrib import admin
from bookbrowser.models import Book, ImageLink, IndustryIdentifier, Author

admin.site.register(Book)
admin.site.register(IndustryIdentifier)
admin.site.register(ImageLink)
admin.site.register(Author)
