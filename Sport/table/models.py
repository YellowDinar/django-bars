from django.db import models

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100)
    kol = models.IntegerField
    point = models.IntegerField
    goal = models.IntegerField
    goal_pass = models.IntegerField
    win = models.IntegerField
    lose = models.IntegerField
    draw = models.IntegerField

class Game(models.Model):
    team1 = models.ForeignKey(Team, to_field='team_id')
    team2 = models.ForeignKey(Team, to_field='team_id')
    score = models.TextField(max_length=5)
    date = models.DateField