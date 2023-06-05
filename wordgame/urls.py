from django.urls import path
from . import views

urlpatterns = [
    path('', views.dictionary_list, name='dictionary_list'),
    path('words/<int:dictionary_id>/', views.word_list, name='word_list'),
    path('game/<int:dictionary_id>/', views.play_game, name='play_game'),
    path('game/result/<int:game_id>/', views.game_result, name='game_result'),   
]