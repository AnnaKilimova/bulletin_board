from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import Ad, UserProfile

# @receiver(post_save, sender=Ad)
# def send_email_on_ad_creation(sender, instance, created, **kwargs):
#     if created:
#         send_mail(
#             'Your ad has been created!',
#             f'Your ad "{instance.title}" has been successfully created.',
#             'noreply@bulletinboard.com',
#             [instance.user.email],
#             fail_silently=False,
#         )
#
# @receiver(post_save, sender=Ad)
# def deactivate_expired_ads(sender, instance, **kwargs):
#     if instance.created_at < timezone.now() - timedelta(days=30):
#         instance.is_active = False
#         instance.save()

@receiver(post_save, sender=Ad)
def deactivate_expired_ads(sender, instance, **kwargs):
    '''A signal for automatic deactivation of ads 30 days after their creation.'''

    if instance.created_at < timezone.now() - timedelta(days=30):
        instance.is_active = False
        instance.save()
