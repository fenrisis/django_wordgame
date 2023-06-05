from django.shortcuts import render, redirect 
from django.http import JsonResponse
from .models import Dictionary, Word, Game
import random


def dictionary_list(request):
    dictionaries = Dictionary.objects.all()
    return render(request, 'dictionary_list.html', {'dictionaries': dictionaries})


def word_list(request, dictionary_id):
    dictionary = Dictionary.objects.get(pk=dictionary_id)
    words = Word.objects.filter(dictionary=dictionary)
    return render(request, 'word_list.html', {'dictionary': dictionary, 'words': words})


def play_game(request, dictionary_id):
    dictionary = Dictionary.objects.get(pk=dictionary_id)
    words = Word.objects.filter(dictionary=dictionary)

    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        game_result = calculate_game_result(user_input, words)
        game = Game(user=request.user, dictionary=dictionary, result=game_result)
        game.save()

        return redirect('game_result', game_id=game.id)

    # Select a random word for translation
    random_word = random.choice(words)
    word_to_translate = random_word.translation

    return render(request, 'game.html', {'dictionary': dictionary, 'word_to_translate': word_to_translate})


def calculate_game_result(user_input, words):
    # Iterate over the words to find a match
    for word in words:
        if user_input.lower() == word.translation.lower():
            return 'Win'
        elif user_input.lower() in word.translation.lower():
            return 'Partial'
    
    return 'Loss'


def game_result(request, game_id):
    game = Game.objects.get(pk=game_id)
    return render(request, 'game_result.html', {'game': game})
