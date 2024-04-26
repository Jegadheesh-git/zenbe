from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user_account = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.user_account