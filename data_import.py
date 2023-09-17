import os
import sqlite3
from django.conf import settings
from src.models import Word, Definition, Example

settings.configure()
connection = sqlite3.connect("./nep_dict.sqlite3")
cursor = connection.cursor()


words = cursor.execute("SELECT * FROM word")

words_obj = []
for id, value, pos in words:
    w = Word(id=id, value=value, part_of_speech=pos)
    words_obj.append(w)

Word.objects.bulk_create(words_obj)

definition = cursor.execute("SELECT * FROM definition")

definition_obj = []
for id, word_id, value in definition:
    d = Definition(id=id, word_id=word_id, value=value)
    definition_obj.append(d)

Definition.objects.bulk_create(definition_obj)


example = cursor.execute("SELECT * FROM example")

example_obj = []
for id, definition_id, value in example:
    d = Example(id=id, definition_id=definition_id, value=value)
    example_obj.append(d)

Example.objects.bulk_create(example_obj)
