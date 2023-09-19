from rest_framework.serializers import ModelSerializer, SerializerMethodField, ReadOnlyField
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter
from .models import Word, Definition, Example

class ExampleSerializer(ModelSerializer):
    class Meta:
        model = Example
        fields = "value",


class DefinitionSerializer(ModelSerializer):
    definition = ReadOnlyField(source="value")
    examples = SerializerMethodField()

    class Meta:
        model = Definition
        fields = "definition", "examples"

    def get_examples(self, obj):
        return obj.examples.values_list("value", flat=True)


class WordSerializer(ModelSerializer):
    word = ReadOnlyField(source="value")
    definitions = DefinitionSerializer(many=True)

    class Meta:
        model = Word
        fields = "word", "part_of_speech", "definitions"


class WordViewSet(ReadOnlyModelViewSet):
    queryset = Word.objects.all().prefetch_related(
        "definitions",
        "definitions__examples"
    )
    serializer_class = WordSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("value", "definitions__value")
