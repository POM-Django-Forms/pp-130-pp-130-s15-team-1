from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic')
    list_filter = ('id', 'name', 'surname', 'patronymic')
    search_fields = ('name',)