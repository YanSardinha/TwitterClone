from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def followers(self):
        return Follow.objects.filter(follow_user = self.user).count()

    @property
    def follows(self):
        return Follow.objects.filter(user = self.user).count()

    def save(self):
        super().save()

class Follow(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'user')
    follower = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'follower')
    date = models.DateTimeField(auto_now_add = True)