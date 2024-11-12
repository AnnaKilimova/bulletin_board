# board/admin.py
from django.contrib import admin
from .models import UserProfile, Category, Ad, Comment

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')

# @admin.register(Ad)
# class AdAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price', 'is_active', 'category', 'user', 'created_at')
#     list_filter = ('is_active', 'category')
#     search_fields = ('title', 'description')
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('ad', 'user', 'created_at')
#     search_fields = ('content',)
#
# @admin.register(UserProfile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'phone_number', 'address')

# Make models available in the admin panel
admin.site.register(UserProfile)
admin.site.register(Category)
# admin.site.register(Ad)
admin.site.register(Comment)

class AdAdmin(admin.ModelAdmin):
    list_filter = ('is_active', 'category')

admin.site.register(Ad, AdAdmin)


