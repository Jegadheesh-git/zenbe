from django.urls import path
from . import views

urlpatterns = [
    path('tournament/all/',views.getAllTournaments),
    path('tournament/<int:id>/',views.getTournamentById),
    path('tournament/add/',views.addTournament),

    path('competition/all/',views.getAllCompetitions),
    path('competition/<int:id>/',views.getCompetitionById),
    path('competition/add/',views.addCompetition),

    path('match/all/',views.getAllMatches),
    path('match/<int:id>/',views.getMatchById),
    path('match/add/',views.addMatch),

    path('stadium/all/',views.getAllStadiums),
    path('stadium/<int:id>/',views.getStadiumById),
    path('stadium/add/',views.addStadium),

    path('team/all/',views.getAllTeams),
    path('team/<int:id>/',views.getTeamById),
    path('team/add/',views.addTeam),
]