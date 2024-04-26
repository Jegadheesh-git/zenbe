from django.db import models
from django.contrib.auth.models import User

class Nationality(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)

class HeightType(models.Model):
    name = models.CharField(max_length=250)

class BowlingType(models.Model):
    description = models.CharField(max_length=250)
    prefix = models.CharField(max_length=250)
    groupId = models.IntegerField()

class BattingType(models.Model):
    name = models.CharField(max_length=250)
    prefix = models.CharField(max_length=250)

class BowlerType(models.Model):
    name = models.CharField(max_length=250)

class Player(models.Model):
    firstName = models.CharField(max_length=250,null=True,default=None, blank=True)
    middleName = models.CharField(max_length=250,null=True,default=None, blank=True)
    lastName = models.CharField(max_length=250,null=True,default=None, blank=True)
    nickName = models.CharField(max_length=250,null=True,default=None, blank=True)
    nationalityId = models.ForeignKey(Nationality,on_delete=models.CASCADE,null=True,default=None, blank=True)
    dob = models.DateField(null=True,default=None, blank=True)
    heightType = models.ForeignKey(HeightType,on_delete=models.CASCADE,null=True,default=None, blank=True)
    gender = models.IntegerField(null=True,default=None, blank=True)
    height = models.FloatField(null=True,default=None, blank=True)
    weight = models.FloatField(null=True,default=None, blank=True)
    batting = models.BooleanField(null=True,default=None, blank=True)
    bowling = models.BooleanField(null=True,default=None, blank=True)
    wicketKeeper = models.BooleanField(null=True,default=None, blank=True)
    fielding = models.BooleanField(null=True,default=None, blank=True)
    bowlingTypeId = models.ForeignKey(BowlingType,on_delete=models.CASCADE,null=True,default=None, blank=True)
    battingTypeId = models.ForeignKey(BattingType,on_delete=models.CASCADE,null=True,default=None, blank=True)
    playerImage = models.ImageField(null=True,default=None, blank=True)
    bowlerTypeId = models.ForeignKey(BowlerType,on_delete=models.CASCADE,null=True,default=None, blank=True)
    pace = models.BooleanField(null=True,default=None, blank=True)
    spin = models.BooleanField(null=True,default=None, blank=True)
    ciPlayerId = models.IntegerField(null=True,default=None, blank=True) 

    createdBy = models.ForeignKey(User,on_delete=models.CASCADE) 
    def save(self, *args, **kwargs):
        # If the user is authenticated, set the current user as createdBy
        if self.createdBy is None and hasattr(self, 'request') and hasattr(self.request, 'user'):
            self.createdBy = self.request.user
        super(Player, self).save(*args, **kwargs)