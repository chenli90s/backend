from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
from .utils import *
# from django.core.paginator import Paginator


# Create your views here.
def login(request):
    user = json.loads(request.body.decode())
    try:
        users = User.objects.get(user_phone=user.get('phone', ''))
        pswd = user.get('pswd', '')
        if users.user_pass == pswd:
            return JsonResponse(resp(True, dict(user_id=users.id,
                                                user_name=users.user_name,
                                                user_pass=users.user_pass,
                                                user_phone=users.user_phone,
                                                user_role=users.user_role,
                                                user_addr=users.user_addr,
                                                user_real=users.user_real, )))
    except  Exception as e:
        print(e)
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
        try:
            db = User.objects.get(user_phone=user.user_phone)
            if db:
                return JsonResponse(resp(False, '手机号已注册'))
        except:
            pass
        user.user_role = post.get('user_role')
        # user.user_addr = post.get('user_addr')
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
        news.news_count = post.get('news_count')
        news.news_price = post.get('news_price')
        news.news_phone = post.get('news_phone')
        user = User.objects.get(id=post.get('user_id'))
        print(user)
        news.auth = user
        news.save()
        return JsonResponse(resp(True, '发布成功'))
    except Exception as e:
        print(e)
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
        news_content = post.get('news_content')
        if news_content:
            news.news_content = news_content
        news_count = post.get('news_count')
        if news_count:
            news.news_count = news_count
        news_price = post.get('news_price')
        if news_price:
            news.news_price = news_price
        news_phone = post.get('news_phone')
        if news_phone:
            news.news_phone = news_phone
        news.save()
        return JsonResponse(resp(True, '修改成功'))
    except Exception as e:
        print(e)
        return JsonResponse(resp(False, '参数错误'))


def news_list(request):
    try:
        data = request.body.decode()
        post = json.loads(data)
        # page_size = post.get('page_size')
        # current_page = post.get('current_page')
        user_role = post.get('user_role')
        pages = News.objects.filter(auth__user_role__contains=user_role).order_by("-news_dt")
        # pages = Paginator(pages, page_size)
        # all_page = pages.count
        # current_list = pages.page(current_page)
        news_lists = []
        for news in pages:
            print(news.news_dt)
            news_lists.append(dict(news_title=news.news_title,
                                   news_dt=news.news_dt.strftime('%Y-%m-%d %H:%M:%S'),
                                   id=news.id,
                                   count=news.news_count,
                                   price=news.news_price,
                                   phone=news.news_phone,
                                   content=news.news_content,
                                   user_role=news.auth.user_role,
                                   user_id=news.auth.id
                                   ))
        return JsonResponse(resp(True, dict(
            # current_page=current_page,
            user_role=user_role,
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
                                            content=news.news_content,
                                            id=news.id,
                                            count=news.news_count,
                                            price=news.news_price,
                                            phone=news.news_phone,
                                            user_role=news.auth.user_role,
                                            )))
    except Exception as e:
        print(e)
        return JsonResponse(resp(False, '参数错误,或id不存在'))

from datetime import datetime
def get_weather(request):
    res = Weather.objects.filter(date_time__gte=datetime.now())
    ls = []
    for ss in res:
        ls.append(dict(info=ss.info, date=ss.date_time.strftime('%Y-%m-%d %H:%M')))
    return JsonResponse(dict(data=ls))


