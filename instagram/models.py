from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from utils.models import BaseModel
from users.models import User
from .managers import PostManager
from django.core.validators import FileExtensionValidator
from instagram.managers import StoryManager


class District(BaseModel):
    title = models.CharField(max_length=31)

    def __str__(self):
        return self.title


class Post(BaseModel):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='post_districts')
    description = models.TextField()

    like_by = models.ManyToManyField(User, related_name='likes', blank=True)
    showed_by = models.ManyToManyField(User, related_name='shows', blank=True)
    saved_by = models.ManyToManyField(User, related_name='savers', blank=True)

    accessibility = models.CharField(max_length=63)
    hide_like_view = models.BooleanField(default=False)
    is_comment = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    post_manager = PostManager()



    def __str__(self):
        return f"{self.description}"



class Media(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='medias')
    media = models.FileField(upload_to='profile/video/', blank=True, null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mpeg', 'jpg', 'png'])])
    set_users = models.ManyToManyField(User, blank=True, related_name='medias')

    def __str__(self):
        return f"{self.post}"

class Following(BaseModel):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_profile')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_by')
    is_confirm = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.profile_id}"


class Story(BaseModel):
    profile = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                related_name='histories')
    media = models.FileField(upload_to='medias/', blank=True, null=True,
                             validators=[FileExtensionValidator(['mp4', 'avi', 'mpeg', 'jpg', 'png'])])
    is_active = models.BooleanField(default=True)
    like_by = models.ManyToManyField(User, related_name='story_likes', blank=True)
    showed_by = models.ManyToManyField(User, related_name='story_watchers', blank=True)
    story_manager = StoryManager()


    def __str__(self):
        return f"{self.profile_id} --> {self.media}"




