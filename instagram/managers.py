from django.db.models import Count
from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.db.models import Q

class UserManager(models.Manager):
    def get_public_users(self):
        queryset = self.get_queryset()
        return queryset.filter(is_private=False)
class PostManager(models.Manager):
    def get_like(self):
        queryset = self.get_queryset()
        return queryset.annotate(likers=Count("like_by"))

    def get_watchers(self):
        queryset = self.get_queryset()
        return queryset.annotate(watchers=Count("showed_by"))

    def get_explore(self):
        queryset = self.get_queryset()
        likers = Q(like_by__gte=1000)
        time_condition = Q(created_at__gte=timezone.now() - timedelta(days=5))
        combined_condition = likers & time_condition
        filtered_queryset = queryset.filter(combined_condition)
        return filtered_queryset


class StoryManager(models.Manager):
    def get_like(self):
        queryset = self.get_queryset()
        return queryset.annotate(likers=Count("like_by"))

    def get_watchers(self):
        queryset = self.get_queryset()
        return queryset.annotate(watchers=Count("showed_by"))

    def get_off_story(self):
        queryset = self.get_queryset()
        return queryset.filter(created_at__gte = timezone.now() - timedelta(hours=24))
