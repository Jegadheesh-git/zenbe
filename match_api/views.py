from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

#tournament end points

@api_view(['GET'])
def getAllTournaments(request):
    tournaments = Tournament.objects.all()
    serializer = TournamentSerializers(tournaments,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTournamentById(request,id):
    try:
        tournament = Tournament.objects.get(id=id)
    except Tournament.DoesNotExist:
        return Response({"message": "Tournament not found"}, status=404)

    serializer = TournamentSerializers(tournament)
    return Response(serializer.data)

@api_view(['POST'])
def addTournament(request):
    serializer = TournamentSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTournament(request,id):
    try:
        tournament = Tournament.objects.get(pk=id)
        tournament.delete()
        return Response({'message':'Deleted successfully!'})
    except Tournament.DoesNotExist as e:
        return Response({'error': 'Tournament does not exist'}, status=404)

#competition end points

@api_view(['GET'])
def getAllCompetitions(request):
    competitions = Competition.objects.all()
    serializer = CompetitionSerializers(competitions,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCompetitionById(request,id):
    try:
        competition = Competition.objects.get(id=id)
    except Competition.DoesNotExist:
        return Response({"message": "Competition not found"}, status=404)

    serializer = CompetitionSerializers(competition)
    return Response(serializer.data)

@api_view(['POST'])
def addCompetition(request):
    serializer = CompetitionSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#match end points

@api_view(['GET'])
def getAllMatches(request):
    matches = Match.objects.all()
    serializer = MatchSerializers(matches,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMatchById(request,id):
    try:
        match = Match.objects.get(id=id)
    except Match.DoesNotExist:
        return Response({"message": "match not found"}, status=404)

    serializer = MatchSerializers(match)
    return Response(serializer.data)

@api_view(['POST'])
def addMatch(request):
    serializer = MatchSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        message = str(serializer.errors)
        response_data = {
            "message": message
        }

        return Response(response_data, status=400)


#stadium end points
@api_view(['GET'])
def getAllStadiums(request):
    stadiums = Stadium.objects.all()
    serializer = StadiumSerializers(stadiums,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStadiumById(request,id):
    try:
        stadium = Stadium.objects.get(id=id)
    except Stadium.DoesNotExist:
        return Response({"message": "stadium not found"}, status=404)
    serializer = StadiumSerializers(stadium)
    return Response(serializer.data)

@api_view(['POST'])
def addStadium(request):
    serializer = StadiumSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#team end-point
@api_view(['GET'])
def getAllTeams(request):
    teams = Team.objects.all()
    serializer = TeamSerializers(teams,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTeamById(request,id):
    try:
        team = Team.objects.get(id=id)
    except Team.DoesNotExist:
        return Response({'message':'team not found'},status=404)
    serializer = TeamSerializers(team)
    return Response(serializer.data)

@api_view(['POST'])
def addTeam(request):
    serializer = TeamSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)