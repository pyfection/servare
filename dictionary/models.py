

from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


def audio_path(instance, filename):
    return 'audio/{}'.format(instance.id)


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Word(models.Model):
    WORD_STATUS = (
        ('SUG', 'Suggested'),
        ('CFR', 'Confirmed'),
        ('RMV', 'Removed'),
    )

    word = models.CharField(max_length=50)
    language = models.ForeignKey(Language)
    tags = models.ManyToManyField(Tag, blank=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    creation_date = models.DateField(auto_now_add=True)
    standard = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=WORD_STATUS)
    synonyms = models.ManyToManyField(
        'self', related_name='synonyms', blank=True
    )
    audio = models.FileField(upload_to=audio_path, blank=True, null=True)

    def __str__(self):
        return self.word


class WordRelation(models.Model):
    first_word = models.ForeignKey(Word, related_name='first_word')
    second_word = models.ForeignKey(Word, related_name='second_word')
    added_by = models.ForeignKey(User, related_name='added_by')
