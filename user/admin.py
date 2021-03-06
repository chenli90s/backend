from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(User)
# admin.site.register(News)


class UserSubInline(admin.TabularInline):
    model = User
    # extra = 5 #默认显示条目的数量

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    #设置哪些字段可以点击进入编辑界面
    list_display = (['user_name','user_phone', 'user_role'])


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    #设置哪些字段可以点击进入编辑界面
    list_display = (['news_title','news_dt', 'news_count', 'news_price', 'news_phone'])
    # inlines = [UserSubInline, ]

@admin.register(Weather)
class NewsAdmin(admin.ModelAdmin):
    #设置哪些字段可以点击进入编辑界面
    list_display = (['info', 'date_time'])
    # inlines = [UserSubInline, ]


