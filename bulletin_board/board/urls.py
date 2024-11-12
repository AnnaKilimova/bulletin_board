from django.urls import path
from . import views

urlpatterns = [
    path('ads/last_month/', views.ads_last_month_view, name='ads_last_month'),
    path('ads/category/<str:category_name>/', views.active_ads_in_category_view, name='active_ads_in_category'),
    path('ads/comment_count/', views.ads_with_comment_count_view, name='ads_with_comment_count'),
    path('ads/user/<int:user_id>/last_month/', views.user_ads_last_month_view, name='user_ads_last_month'),
]

