from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from table.models import Team

def index(request):
    teams = Team.objects.all()
    return render(request, 'table/index.html', {'teams':teams})