from users.models import User
from instagram.models import Story, Post, Media
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    following = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = (
            "website",
            "bio",
            "gender",
            "suggestions",
            "is_private",
            "closed_friends",
            "muted_accounts",
            "blocked_users",
            "saved_posts",
            "photo",
            "avatar",
            "following",
        )

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            'post',
            'media',
        )

class PostExploreSerializer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField()
    medias = MediaSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = (
            'profile',
            'medias',
        )

class PostSerializer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = (
            'profile',
            'district',
            'description',
            'like_by',
            'showed_by',
            'saved_by',
            'accessibility',
            'hide_like_view',
            'is_comment',
            'is_deleted',
            'post_manager'
        )






class StoryActiveSerializer2(serializers.ModelSerializer):
    profile = serializers.StringRelatedField()
    class Meta:
        model = Story
        fields = (
            "profile",
            "media",
        )


