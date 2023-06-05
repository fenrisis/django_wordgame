from django.contrib import admin
from .models import Dictionary, Word, Game

admin.site.register(Dictionary)
admin.site.register(Word)
admin.site.register(Game)