from django.urls import path
from .views import *

urlpatterns = [
    path('login', login),
    path('regist', regist),
    path('addNews', add_new),
    path('delNews', del_news),
    path('upNews', up_news),
    path('newsList', news_list),
    path('newsDetail', news_detail),
    path('weather', get_weather)
]