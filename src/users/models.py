from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.CharField(max_length=250, blank=True, null=True, default='No bio.')

    level = models.CharField(max_length=50, default='Beginner')
    rank = models.ImageField(default='ranks/beginner.png')

    attending_course = models.CharField(max_length=100, blank=True, null=True, default='Python 3: From zero to hero')

    chapter_studying = models.PositiveIntegerField(default=1)
    test_taking = models.PositiveIntegerField(default=0)

    test_1_times = models.PositiveIntegerField(default=0)
    test_1_total = models.PositiveIntegerField(default=0)
    test_1_correct = models.PositiveIntegerField(default=0)
    test_1_wrong = models.PositiveIntegerField(default=0)
    test_1_success_rate = models.FloatField(default=0.0)

    test_2_times = models.PositiveIntegerField(default=0)
    test_2_total = models.PositiveIntegerField(default=0)
    test_2_correct = models.PositiveIntegerField(default=0)
    test_2_wrong = models.PositiveIntegerField(default=0)
    test_2_success_rate = models.FloatField(default=0.0)

    test_3_times = models.PositiveIntegerField(default=0)
    test_3_total = models.PositiveIntegerField(default=0)
    test_3_correct = models.PositiveIntegerField(default=0)
    test_3_wrong = models.PositiveIntegerField(default=0)
    test_3_success_rate = models.FloatField(default=0.0)

    bad_at = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

