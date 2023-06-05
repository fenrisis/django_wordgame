from django.db import models
from django.contrib.auth.models import User

class Dictionary(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Word(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE)
    word_text = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.word_text} ({self.translation}) - Points: {self.points}"
    

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE)
    result = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} - {self.dictionary.name} - {self.result}"