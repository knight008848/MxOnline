from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birth_day = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), default='male', max_length=10, verbose_name=u'性别')
    address = models.CharField(max_length=100, null=True, verbose_name=u'地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号码')
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', null=True, blank=True)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱地址')
    send_type = models.CharField(choices=(('register', u'注册'), ('forget', u'找回密码')), max_length=10, verbose_name=u'类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = u'验证码'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name=u'图片', max_length=100)
    url = models.URLField(max_length=200, verbose_name=u'URL')
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name
