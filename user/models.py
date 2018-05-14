from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.TextField(max_length=50)
    user_pass = models.TextField(max_length=50)
    user_phone = models.TextField(max_length=50)
    user_role = models.TextField(max_length=50)
    user_num = models.TextField(max_length=50)
    user_addr = models.TextField(max_length=50)
    user_real = models.TextField(max_length=50)


class Goods(models.Model):
    good_name = models.TextField(max_length=50)
    good_price = models.TextField(max_length=50)
    good_desc = models.TextField(max_length=50)
    good_count = models.TextField(max_length=50)
    good_phone = models.TextField(max_length=50)
    good_img = models.TextField(max_length=50)
    good_user = models.ForeignKey(User, on_delete=None)


class News(models.Model):
    news_title = models.TextField(max_length=50)
    news_dt = models.DateTimeField(auto_now=True)
    news_content = models.TextField(max_length=500)
    auth = models.ForeignKey(User, on_delete=None)
