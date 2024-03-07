from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _
from django.db import models
from utils.choices import Gender
from instagram.managers import UserManager


class User(AbstractUser):

    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    website = models.URLField(blank=True, null=True)
    bio = models.TextField(null=True, blank=True)

    gender = models.CharField(max_length=32, choices=Gender.choices, default=Gender.PREFER_NOT_TO_SAY)
    suggestions = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)
    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='follower_users')

    muted_accounts = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='muting')
    closed_friends = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='friends')
    blocked_users = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='blocked')

    saved_posts = models.ForeignKey('instagram.Post', on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    user_manager=UserManager()

    def __str__(self):
        return f"{self.username}"




































