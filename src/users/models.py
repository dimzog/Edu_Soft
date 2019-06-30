from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    level = models.CharField(max_length=50, default='Beginner')
    rank = models.ImageField(default=f'ranks/Beginner.png')

    attending_course = models.CharField(max_length=100, blank=True, null=True, default='Python 3: From zero to hero')

    chapter_studying = models.PositiveIntegerField(default=1)
    test_taking = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.user.username} Profile'


