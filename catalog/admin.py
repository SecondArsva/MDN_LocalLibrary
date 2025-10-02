from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language

# Register your models here.

# Registro Simple
#admin.site.register(Author)
#admin.site.register(Book)
#admin.site.register(BookInstance)

#* Configurar un mostrado avanzado mediante una clase ModelAdmin
#  en los casos de Modelos de un solo campo, es innecesario.
#  Por ello se establece el registro simple.*#
admin.site.register(Genre)
admin.site.register(Language)

class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    can_delete = False
    #show_change_link = True
    readonly_fields = ('title', 'isbn', 'summary', 'genre', 'language')

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ('first_name', 'last_name', ('date_of_birth', 'date_of_death'))
    inlines = [BookInline]
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

# Challenge yourself
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'uniqueid')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'uniqueid')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
