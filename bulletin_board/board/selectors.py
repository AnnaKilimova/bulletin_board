from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from .models import Ad, Category

def get_ads_last_month():
    last_month = timezone.now() - timedelta(days=30)
    return Ad.objects.filter(created_at__gte=last_month)

def get_active_ads_in_category(category_name):
    category = Category.objects.get(name=category_name)
    return Ad.objects.filter(category=category, is_active=True)

def get_ads_with_comment_count():
    return Ad.objects.annotate(comment_count=Count('comments'))

def get_user_ads_last_month(user):
    last_month = timezone.now() - timedelta(days=30)
    return Ad.objects.filter(user=user, created_at__gte=last_month)
