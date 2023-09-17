from django.db import models

# Create your models here.

class Word(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    value = models.CharField(max_length=255)
    part_of_speech = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.value

class Definition(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name="definitions")
    value = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.value


class Example(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    definition = models.ForeignKey(Definition, on_delete=models.CASCADE, related_name="examples")
    value = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.value
