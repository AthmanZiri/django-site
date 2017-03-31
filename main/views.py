from django.shortcuts import render

def index(request):
	return render(request, 'index.html', {})


def team(request):
	team_sisi ='hello mates!'
	return render(request, 'team.html', {'team_sisi': team_sisi})