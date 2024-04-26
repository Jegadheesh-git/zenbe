from django.shortcuts import render,redirect,get_object_or_404
from match_api.models import Tournament,Competition,Match
from .forms import TournamentForm, CompetitionForm, MatchForm

# Create your views here.
def displayTournamentDashboard(request):
    if request.method == 'POST':
        tournaments = Tournament.objects.filter(createdBy=request.user)
        return render(request,'tournament_dashboard.html',{'tournaments':tournaments})
    else:
        tournaments = Tournament.objects.filter(createdBy=request.user)
        return render(request,'tournament_dashboard.html',{'tournaments':tournaments})
    
def addTournament(request):
    if request.method == 'POST':
        tournament_name = request.POST['name']
        createdBy = request.user
        tournament = Tournament(name=tournament_name,createdBy=createdBy)
        tournament.save()
        return redirect('tournament_dashboard')
    else:
        return render(request,'add_tournament.html')

def updateTournament(request,pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if request.method == 'POST':
        form = TournamentForm(request.POST, instance=tournament)
        if form.is_valid():
            form.save()
            return redirect('tournament_dashboard')
    else:
        form = TournamentForm(instance=tournament)
        return render(request,'update_tournament.html',{'form':form})

def deleteTournament(request,pk):
    tournament = get_object_or_404(Tournament,pk=pk)
    if request.method == 'POST':
        tournament.delete()
        return redirect('tournament_dashboard')
    else:
        return render(request,'tournament_delete.html',{'tournament':tournament})
def displayCompetitionDashboard(request,tournament_id):
    competitions = Competition.objects.filter(createdBy = request.user,tournament=tournament_id)
    return render(request,'competition_dashboard.html',{'competitions':competitions})

def addCompetition(request):
    if request.method == 'POST':
        
        form = CompetitionForm(request.POST)
        if form.is_valid():
            competition = form.save(commit=False)
            competition.createdBy = request.user  # Assign the current user to createdBy field
            competition.save() # This will save the data to the database
            
    else:
        form = CompetitionForm()
    return render(request, 'add_competition.html', {'form': form})

def updateCompetition(request,pk):
    competition = get_object_or_404(Competition, pk=pk)
    if request.method == 'POST':
        form = CompetitionForm(request.POST, instance=competition)
        if form.is_valid():
            form.save()
            return redirect('competition_dashboard',pk)
    else:
        form = CompetitionForm(instance=competition)
        return render(request,'update_competition.html',{'form':form})
    

def deleteCompetition(request,pk):
    competition = get_object_or_404(Competition,pk=pk)
    tournament_id = competition.tournament.id
    if request.method == 'POST':
        competition.delete()
        return redirect('competition_dashboard',tournament_id)
    else:
        return render(request,'competition_delete.html',{'competition':competition})

def displayMatches(request,competition_id):
    matches = Match.objects.filter(createdBy=request.user,competition=competition_id)
    print(matches)
    return render(request,'match_dashboard.html',{'matches':matches})

def addMatch(request):
    if request.method == 'POST':
        print('entered')
        form = MatchForm(request.POST)
        if form.is_valid():
            match = form.save(commit=False)
            match.createdBy = request.user  # Assign the current user to createdBy field
            match.save() # This will save the data to the database
            
    else:
        form = MatchForm()
    return render(request,'add_match.html',{'form':form})

def updateMatch(request,pk):
    match = get_object_or_404(Match, pk=pk)
    competition_id = match.competition.id
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('display_matches',competition_id)
    else:
        form = MatchForm(instance=match)
        return render(request,'update_match.html',{'form':form})
    
def deleteMatch(request,pk):
    match = get_object_or_404(Match,pk=pk)
    competition_id = match.competition.id
    if request.method == 'POST':
        match.delete()
        return redirect('display_matches',competition_id)
    else:
        return render(request,'match_delete.html',{'match':match})