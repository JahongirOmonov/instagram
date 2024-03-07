from django.shortcuts import render
from .serializers import (UserSerializer,
                          StoryActiveSerializer2,
                          PostExploreSerializer, PostSerializer)
from rest_framework import generics
from users.models import User
from instagram.models import Story, Post
from django.utils import timezone
from datetime import timedelta


# Create your views here.

class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserPublicListApiView(generics.ListAPIView):
    queryset = User.user_manager.get_public_users()
    serializer_class = UserSerializer



class PostExploreListApiView(generics.ListAPIView):
    queryset = Post.post_manager.get_explore()
    serializer_class = PostExploreSerializer

class PostDetailApiView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class StoryActiveListApiView2(generics.ListAPIView):
    queryset = Story.story_manager.get_off_story()
    serializer_class = StoryActiveSerializer2

    # def get_queryset(self):
    #     queryset = super().queryset
    #     if self.request.query_params.get('is_active', None) is True:
    #         queryset = queryset.filter(created_at__gte=timezone.now() - timedelta(hours=24))
    #         return queryset
    #     return queryset
