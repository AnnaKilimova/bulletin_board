from django.shortcuts import render
from .selectors import (
    get_ads_last_month,
    get_active_ads_in_category,
    get_ads_with_comment_count,
    get_user_ads_last_month
)


# http://127.0.0.1:8000/board/ads/last_month/
def ads_last_month_view(request):
    ads = get_ads_last_month()
    return render(request, 'board/ads_last_month.html', {'ads': ads})


# http://127.0.0.1:8000/board/ads/category/Fashion/
def active_ads_in_category_view(request, category_name):
    ads = get_active_ads_in_category(category_name)
    return render(request, 'board/active_ads_in_category.html', {'ads': ads, 'category_name': category_name})


# http://127.0.0.1:8000/board/ads/comment_count/
def ads_with_comment_count_view(request):
    ads = get_ads_with_comment_count()
    return render(request, 'board/ads_with_comment_count.html', {'ads': ads})


# http://127.0.0.1:8000/board/ads/user/1/last_month/
def user_ads_last_month_view(request, user_id):
    ads = get_user_ads_last_month(user_id)
    return render(request, 'board/user_ads_last_month.html', {'ads': ads})

