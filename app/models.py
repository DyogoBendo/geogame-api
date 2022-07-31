from django.db import models

class Game(models.Model):
    player = models.CharField(max_length = 50)
    score = models.PositiveSmallIntegerField()
    time = models.PositiveBigIntegerField()
    date = models.DateTimeField(auto_now = True)
