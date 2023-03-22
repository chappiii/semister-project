from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids')
)

MOVIE_CHOICES = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single'),
)

GENER_CHOICES = (
    ('action', 'action'),
    ('comedy', 'comedy'),
    ('romantic', 'romantic'),
    ('amharic', 'amharic'),
    ('drama', 'drama'),
)


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('profile', blank=True)


class Profile(models.Model):
    name = models.CharField(max_length=225)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4)


class Movie(models.Model):
    title: str = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=10, choices=MOVIE_CHOICES)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    gener = models.CharField(
        max_length=10, choices=GENER_CHOICES, default='action')


class Video(models.Model):
    title: str = models.CharField(max_length=225, blank=True, null=True)
    file = models.FileField(upload_to='movies')
