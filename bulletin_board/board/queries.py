from django.utils import timezone
from datetime import timedelta
from .models import Ad, Category, Comment, User

# Усі оголошення, створені за останній місяць
recent_ads = Ad.objects.filter(created_at__gte=timezone.now() - timedelta(days=30))

# Усі активні оголошення в певній категорії
def active_ads_in_category(category_id):
    return Ad.objects.filter(category_id=category_id, is_active=True)

# Кількість коментарів до кожного оголошення
ads_with_comments_count = Ad.objects.annotate(num_comments=models.Count('comments'))

# Усі оголошення певного користувача
def ads_by_user(user_id):
    return Ad.objects.filter(user_id=user_id)
