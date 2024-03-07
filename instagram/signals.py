# from .models import Story
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from datetime import timedelta
# from django.utils import timezone
#
# @receiver(post_save, sender=Story)
# def deactivate_inactive_stories(sender, instance, created, **kwargs):
#     if created:
#         instance_created_at = instance.created_at
#         expiration_time = instance_created_at + timedelta(hours=24)
#         if timezone.now() >= expiration_time:
#             instance.is_active = False
#             instance.save(update_fields=['is_active'])
