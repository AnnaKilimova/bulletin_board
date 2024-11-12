from django.db import models
from django.contrib.auth.models import User  # User model taken from Django.
from django.utils import timezone
from datetime import timedelta
from django.core.validators import MinValueValidator



# Create basic models for users, categories, ads, comments.


class UserProfile(models.Model):
    """Extend the user profile with an additional model (phone_number, address)."""

    # One record in one table (model) corresponds to only one record in another table.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


class Category(models.Model):
    """Describes ad categories."""

    name = models.CharField(max_length=100, unique=True)  # A unique field for the category name.
    description = models.TextField(blank=True)  # Field for category description.

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def active_ads_count(self):
        """Returns the number of active ads in the category."""
        return self.ads.filter(is_active=True).count()


class Ad(models.Model):
    """Describes ads created by users."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    # One record in the first model can be linked to several records in the second model.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ads")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="ads")

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_ad", "Може додавати оголошення"),
        ]

    def short_description(self):
        """For turning a short description."""
        return (self.description[:100] + "..." if len(self.description) > 100 else self.description)

    def deactivate_if_expired(self):
        """Automatically makes the ad inactive if 30 days have passed."""
        if self.created_at < timezone.now() - datetime.timedelta(days=30):
            self.is_active = False
            self.save()


class Comment(models.Model):
    """Comments to ads."""

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # One record in the first model can be linked to several records in the second model.
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment by {self.user.username} on {self.ad.title}"

