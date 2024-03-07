from django.db import models

from users.models import User
from instagram.models import Post
from utils.models import BaseModel
from instagram.models import Story


class Message(BaseModel):
    content = models.TextField()
    reply = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies", blank=True, null=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="user_message")

    def __str__(self) -> str:
        return self.content[:16]


class UserMessage(BaseModel):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_sent")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_received")
    message = models.ForeignKey( Message, on_delete=models.CASCADE, related_name="user_message")

    def __str__(self) -> str:
        return f"{self.from_user_id} to {self.to_user_id}"


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usercomments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postcomments")

    content = models.TextField()

    reply = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies", blank=True, null=True)
    users_liked = models.ManyToManyField(User, related_name="comments_liked", blank=True)

    def __str__(self) -> str:
        return f"{self.user_id} to {self.post_id}"
