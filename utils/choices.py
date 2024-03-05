from django.db import models



class Gender(models.TextChoices):
    FEMALE = 'Female'
    MALE = 'Male'
    CUSTOM = 'Custom'
    PREFER_NOT_TO_SAY = 'Prefer not to say'
