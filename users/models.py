from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from utils.models import BaseModel
from django.db import models
from utils.choices import Gender
from django.core.validators import FileExtensionValidator


class User(AbstractUser):
    """
    Default custom user model for My Awesome Project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    website = models.URLField(blank=True, null=True)
    bio = models.TextField()
    gender = models.CharField(max_length=32, choices=Gender.choices, default=Gender.PREFER_NOT_TO_SAY)
    suggestions = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)
    # archive = models.ManyToManyField('ProfileHistory', related_name='archive_medias', blank=True)

    def __str__(self):
        return f"{self.user}"


class Follower(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follower_profile')
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follower_by')
    is_confirm = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.profile}"


class Following(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="following_owner")
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="following_to")
    is_confirm = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.profile}"


# class Archive(BaseModel):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='archives')
#     image = models.ForeignKey('Image', on_delete=models.CASCADE, related_name='images', blank=True, null=True)
#     video = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='videos', blank=True, null=True)
#     is_active = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.profile


class Image(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='images_profile')
    image = models.FileField(upload_to='images/',
                             validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])

    def __str__(self):
        return f"{self.profile}"


class ProfileHistory(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                related_name='histories')
    media = models.FileField(upload_to='medias/', blank=True, null=True,
                             validators=[FileExtensionValidator(['mp4', 'avi', 'mpeg', 'jpg', 'png'])])
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.profile}"


































