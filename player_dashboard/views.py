from django.shortcuts import render,get_object_or_404, redirect
from player_api.models import Player
from .forms import PlayerForm
from django.contrib.auth.decorators import login_required

@login_required
def displayHome(request):
    if request.method=='POST':
        name = request.POST['name']
        results = Player.objects.filter(nickName__icontains=name)
        print(results)
        return render(request,'player_dashboard.html',{'results':results})
    else:
        results = Player.objects.filter(createdBy = request.user)
        return render(request,'player_dashboard.html',{'results':results})

@login_required
def getPlayerData(request,pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request,'get_player.html',{'player':player})

@login_required
def addPlayer(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.createdBy = request.user  # Assign the current user to createdBy field
            player.save() # This will save the data to the database
            
    else:
        form = PlayerForm()
    return render(request, 'add_player.html', {'form': form})

@login_required
def update_player(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect('getplayer',pk=pk)  # Redirect to player detail page
    else:
        form = PlayerForm(instance=player)
    return render(request, 'update_player.html', {'form': form})

@login_required
def delete_player(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('home')  # Redirect to home page or any other page after deletion
    return render(request, 'confirm_delete.html', {'player': player})
