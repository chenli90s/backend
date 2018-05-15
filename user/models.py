from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.TextField(verbose_name='用户名',max_length=50,default=None,blank=True, null=True)
    user_pass = models.TextField(verbose_name='密码',max_length=50,default=None,blank=True, null=True)
    user_phone = models.TextField(verbose_name='手机号',max_length=50,default=None,blank=True, null=True)
    user_role = models.TextField(verbose_name='角色',max_length=50,default=None,blank=True, null=True)
    user_num = models.TextField(verbose_name='用户编号',max_length=50,default=None, blank=True, null=True)
    user_addr = models.TextField(verbose_name='用户地址',max_length=50,default=None,blank=True, null=True)
    user_real = models.TextField(verbose_name='实名',max_length=50,default=None,blank=True, null=True)
    class Meta:
        verbose_name_plural = "账号"

class Goods(models.Model):
    good_name = models.TextField(max_length=50,default=None,blank=True, null=True)
    good_price = models.TextField(max_length=50,default=None,blank=True, null=True)
    good_desc = models.TextField(max_length=50,default=None,blank=True, null=True)
    good_count = models.TextField(max_length=50,default=None,blank=True, null=True)
    good_phone = models.TextField(max_length=50,default=None,blank=True, null=True)
    good_img = models.TextField(max_length=50,default=None,blank=True, null=True)
    good_user = models.ForeignKey(User, on_delete=None)


class News(models.Model):
    news_title = models.TextField(verbose_name='标题',max_length=50,default=None,blank=True, null=True)
    news_dt = models.DateTimeField(verbose_name='创建时间',auto_now=True,blank=True, null=True)
    news_count = models.TextField(verbose_name='数量',max_length=11,default=None,blank=True, null=True)
    news_price = models.TextField(verbose_name='价格',max_length=12,default=None,blank=True, null=True)
    news_phone = models.TextField(verbose_name='联系电话',max_length=11,default=None,blank=True, null=True)
    news_content = models.TextField(verbose_name='内容',max_length=500,default=None,blank=True, null=True)
    auth = models.ForeignKey(User, on_delete=None, verbose_name='发布者',)
    class Meta:
        verbose_name_plural = "信息"
