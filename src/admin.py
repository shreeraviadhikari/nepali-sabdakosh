from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

# Register your models here.

from .models import Definition, Word

class ReadOnlyMixin:
    def has_add_permission(self, *args, **kwargs) -> bool:
        return False

    def has_delete_permission(self, *args, **kwargs) -> bool:
        return False

    def has_change_permission(self, *args, **kwargs) -> bool:
        return False


class DefinitionAdmin(admin.TabularInline):
    model = Definition
    fields = ("value", "examples")
    list_display = ("value", "examples")
    search_fields = ("value",)
    readonly_fields = "examples",

    def examples(self, obj):
        return "\n".join(obj.examples.values_list("value", flat=True))


class WordAdmin(ReadOnlyMixin, admin.ModelAdmin):
    model = Word
    list_display = ("value", "definitions", "part_of_speech")
    search_fields = ["value", "definitions__value"]
    inlines = [DefinitionAdmin]



    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return Word.objects.all().prefetch_related("definitions")

    def definitions(self, obj):
        return "\n".join(obj.definitions.values_list("value", flat=True))

admin.site.register(Word, WordAdmin)
