from django.urls import path
from .views import *

urlpatterns = [
    path('',displayTournamentDashboard,name='tournament_dashboard'),
    path('add_tournament/',addTournament,name='add_tournament'),
    path('update_tournament/<int:pk>/',updateTournament,name='update_tournament'),
    path('delete_tournament/<int:pk>/',deleteTournament,name='delete_tournament'),
    path('display_competitions/<int:tournament_id>/',displayCompetitionDashboard,name='competition_dashboard'),
    path('add_competition/',addCompetition,name='add_competition'),
    path('update_competition/<int:pk>/',updateCompetition,name='update_competition'),
    path('delete_competition/<int:pk>/',deleteCompetition,name='delete_competition'),
    path('display_matches/<int:competition_id>/',displayMatches,name='display_matches'),
    path('add_match/',addMatch,name='add_match'),
    path('update_match/<int:pk>/',updateMatch,name='update_match'),
    path('delete_match/<int:pk>/',deleteMatch,name='delete_match'),
]