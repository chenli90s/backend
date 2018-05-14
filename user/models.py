from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.TextField(max_length=50,default=None)
    user_pass = models.TextField(max_length=50,default=None)
    user_phone = models.TextField(max_length=50,default=None)
    user_role = models.TextField(max_length=50,default=None)
    user_num = models.TextField(max_length=50,default=None)
    user_addr = models.TextField(max_length=50,default=None)
    user_real = models.TextField(max_length=50,default=None)


class Goods(models.Model):
    good_name = models.TextField(max_length=50,default=None)
    good_price = models.TextField(max_length=50,default=None)
    good_desc = models.TextField(max_length=50,default=None)
    good_count = models.TextField(max_length=50,default=None)
    good_phone = models.TextField(max_length=50,default=None)
    good_img = models.TextField(max_length=50,default=None)
    good_user = models.ForeignKey(User, on_delete=None)


class News(models.Model):
    news_title = models.TextField(max_length=50,default=None)
    news_dt = models.DateTimeField(auto_now=True)
    news_count = models.TextField(max_length=11,default=None)
    news_price = models.TextField(max_length=12,default=None)
    news_phone = models.TextField(max_length=11,default=None)
    news_content = models.TextField(max_length=500,default=None)
    auth = models.ForeignKey(User, on_delete=None)
