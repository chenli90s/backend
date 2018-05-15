from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(User)
# admin.site.register(News)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    #设置哪些字段可以点击进入编辑界面
    list_display = (['user_name','user_phone', 'user_role'])

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    #设置哪些字段可以点击进入编辑界面
    list_display = (['news_title','news_dt', 'news_count', 'news_price', 'news_phone'])