from django.test import TestCase

# Create your tests here.

from .models import Ad, Category, Comment, User
from django.utils import timezone
from datetime import timedelta

class AdModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.category = Category.objects.create(name="Test Category", description="Test description")
        self.ad = Ad.objects.create(
            title="Test Ad",
            description="Test description for ad",
            price=10.0,
            user=self.user,
            category=self.category,
            created_at=timezone.now() - timedelta(days=31)
        )

    def test_ad_deactivation(self):
        self.ad.deactivate_if_expired()
        self.assertFalse(self.ad.is_active)

    def test_ad_short_description(self):
        self.assertEqual(self.ad.short_description(), "Test description for ad"[:100])

class CategoryModelTest(TestCase):
    def test_active_ads_count(self):
        # Test logic for counting active ads
        pass

