from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=15)

    def __str__(self):
        return self.nama
    

class Messages(models.Model):
    profil = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pesan = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.profil, self.pesan)

    