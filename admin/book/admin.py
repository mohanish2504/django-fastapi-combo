from django.contrib import admin
from book.models import Book,Author

admin.site.register(Book)
admin.site.register(Author)