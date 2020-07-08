from django.contrib import admin
from bookbrowser.models import Book, ImageLink, IndustryIdentifier, Author


class BookAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass


class ImageLinkAdmin(admin.ModelAdmin):
    pass


class IndustryIdentifierAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(IndustryIdentifier, IndustryIdentifierAdmin)
admin.site.register(ImageLink, ImageLinkAdmin)
admin.site.register(Author, AuthorAdmin)
