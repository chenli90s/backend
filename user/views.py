from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
from .utils import *
from django.core.paginator import Paginator


# Create your views here.
def login(request):
    user = json.loads(request.body.decode())
    try:
        users = User.objects.get(user_name=user.get('name', ''))
        if not users.user_pass is user.get('pswd', ''):
            return JsonResponse(resp(True, dict(user_id=users.id,
                                                user_name=users.user_name,
                                                user_pass=users.user_pass,
                                                user_phone=users.user_phone,
                                                user_role=users.user_role,
                                                user_addr=users.user_addr,
                                                user_real=users.user_real, )))
    except  Exception as e:
        return JsonResponse(resp(False, '密码或用户名错误'))
    return JsonResponse(resp(False, '密码或用户名错误'))


def regist(request):
    try:
        data = request.body.decode()
        post = json.loads(data)
        user = User()
        user.user_name = post.get('user_name')
        user.user_pass = post.get('user_pass')
        user.user_phone = post.get('user_phone')
        user.user_role = post.get('user_role')
        user.user_addr = post.get('user_addr')
        user.user_real = post.get('user_real')
        user.save()
    except Exception as e:
        print(e)
        return JsonResponse(resp(False, '参数错误'))
    return JsonResponse(resp(True, '注册成功'))


def add_new(request):
    try:
        data = request.body.decode()
        post = json.loads(data)
        news = News()
        news.news_title = post.get('news_title')
        news.news_content = post.get('news_content')
        user = User.objects.get(id=post.get('user_id'))
        news.auth = user
        news.save()
        return JsonResponse(resp(True, '发布成功'))
    except Exception as e:
        return JsonResponse(resp(False, '参数错误'))


def del_news(request):
    try:
        data = request.body.decode()
        post = json.loads(data)
        news = News.objects.get(id=post.get('news_id'))
        news.delete()
        return JsonResponse(resp(True, '删除成功'))
    except Exception as e:
        return JsonResponse(resp(False, '参数错误'))

from datetime import datetime
def up_news(request):
    try:
        data = request.body.decode()
        post = json.loads(data)
        news = News.objects.get(id=post.get('news_id'))
        if post.get('news_title'):
            news.news_title = post.get('news_title')
        # if post.get('news_dt'):
        #     # news.news_dt = datetime.strptime(post.get('news_dt'), '%Y-%m-%d %H:%M:%S')
        #     news.news_dt = post.get('news_dt')
        if post.get('news_content'):
            news.news_content = post.get('news_content')
        news.save(force_update=True)
        return JsonResponse(resp(True, '修改成功'))
    except Exception as e:
        print(e)
        return JsonResponse(resp(False, '参数错误'))


def news_list(request):
    try:
        data = request.body.decode()
        post = json.loads(data)
        page_size = post.get('page_size')
        current_page = post.get('current_page')
        pages = News.objects.all().order_by("-news_dt")
        pages = Paginator(pages, page_size)
        all_page = pages.count
        current_list = pages.page(current_page)
        news_lists = []
        for news in current_list:
            print(news.news_dt)
            news_lists.append(dict(news_title=news.news_title,news_dt=news.news_dt.strftime('%Y-%m-%d %H:%M:%S'), id=news.id))
        return JsonResponse(resp(True, dict(
            current_page=current_page,
            all_page=all_page,
            news=news_lists
        )))
    except Exception as e:
        print(e)
        return JsonResponse(resp(False, '参数错误'))

def news_detail(request):
    try:
        data = request.body.decode()
        post = json.loads(data)
        id = post.get('news_id')
        news = News.objects.get(id=id)
        return JsonResponse(resp(True, dict(title=news.news_title,
                                            date=news.news_dt.strftime('%Y-%m-%d %H:%M:%S'),
                                            content=news.news_content)))
    except Exception as e:
        print(e)
        return JsonResponse(resp(False, '参数错误,或id不存在'))