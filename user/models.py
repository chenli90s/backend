from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.TextField(max_length=50,default=None,blank=True, null=True)
    user_pass = models.TextField(max_length=50,default=None,blank=True, null=True)
    user_phone = models.TextField(max_length=50,default=None,blank=True, null=True)
    user_role = models.TextField(max_length=50,default=None,blank=True, null=True)
    user_num = models.TextField(max_length=50,default=None, blank=True, null=True)
    user_addr = models.TextField(max_length=50,default=None,blank=True, null=True)
    user_real = models.TextField(max_length=50,default=None,blank=True, null=True)


class Goods(models.Model):
    good_name = models.TextField(max_length=50,default=None,blank=True, null=True)
    good_price = models.TextField(max_length=50,default=None,blank=True, null=True)
    good_desc = models.TextField(max_length=50,default=None,blank=True, null=True)
    good_count = models.TextField(max_length=50,default=None,blank=True, null=True)
    good_phone = models.TextField(max_length=50,default=None,blank=True, null=True)
    good_img = models.TextField(max_length=50,default=None,blank=True, null=True)
    good_user = models.ForeignKey(User, on_delete=None)


class News(models.Model):
    news_title = models.TextField(max_length=50,default=None,blank=True, null=True)
    news_dt = models.DateTimeField(auto_now=True,blank=True, null=True)
    news_count = models.TextField(max_length=11,default=None,blank=True, null=True)
    news_price = models.TextField(max_length=12,default=None,blank=True, null=True)
    news_phone = models.TextField(max_length=11,default=None,blank=True, null=True)
    news_content = models.TextField(max_length=500,default=None,blank=True, null=True)
    auth = models.ForeignKey(User, on_delete=None)
