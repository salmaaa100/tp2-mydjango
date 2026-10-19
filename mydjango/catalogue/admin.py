from django.contrib import admin

from .models import Author, Book , Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description_preview")
    search_fields = ("name", "description")

    @admin.display(description="Aperçu")
    def description_preview(self, obj):
        text = obj.description
        return text if len(text) <= 60 else f"{text[:60]}…"
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Affichage personnalisé pour les livres."""

    list_display = ("title", "author", "price", "publication_date")
    list_filter = ("publication_date", "author")
    search_fields = ("title", "summary")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Enregistrement simple pour les auteurs."""

    list_display = ("last_name", "first_name", "email", "joined_date")
    search_fields = ("last_name", "email")