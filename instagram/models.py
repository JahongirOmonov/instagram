from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from utils.models import BaseModel
from users.models import Profile


class District(BaseModel):
    title = models.CharField(max_length=31)

    def __str__(self):
        return self.title

class Post(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_profiles')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='post_districts')
    description = models.TextField()

    like = models.ManyToManyField(Profile, related_name='post_likes', blank=True)
    accessibility = models.CharField(max_length=63)
    hide_like_view = models.BooleanField(default=False)
    is_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.profile

class Content(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='contents_profile')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='contents')

    like = models.ManyToManyField(Profile, related_name='contents_like', blank=True)
    comment = models.TextField()
    parent = models.ManyToManyField('self', related_name='children')

    def __str__(self):
        return self.profile




class Media(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='medias')
    media = models.FileField(upload_to='profile/video/', blank=True, null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mpeg', 'jpg', 'png'])])
    set_users = models.ManyToManyField(Profile, blank=True, related_name='medias')

    def __str__(self):
        return f"{self.post}"




