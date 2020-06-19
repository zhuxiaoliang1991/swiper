from django.db import models
import datetime

# Create your models here.
from lib.orm import ModelMixin
from vip.models import Vip


class User(models.Model):
    '''用户数据模型'''
    nickname = models.CharField(max_length=32,unique=True,verbose_name='昵称')
    phonenum = models.CharField(max_length=16,unique=True,verbose_name='手机号')
    sex = models.CharField(max_length=8,choices=(('男','男'),('女','女')),verbose_name='性别')
    birth_year = models.IntegerField(default=2000,verbose_name='出生年份')
    birth_month = models.IntegerField(default=1,verbose_name='出生月份')
    birth_day = models.IntegerField(default=1,verbose_name='出生日期')
    avatar = models.CharField(max_length=256,verbose_name='头像url')
    location = models.CharField(max_length=32,verbose_name='常居地址')
    vip_id = models.IntegerField(default=1)

    @property
    def age(self):
        now = datetime.date.today()
        birth_date = datetime.date(
            self.birth_year,self.birth_month,self.birth_day
        )
        #返回年龄
        return (now - birth_date).days//365

    #创建user与profile两表之间的关联关系
    @property
    def profile(self):
        '''用户的配置项'''
        # if '_profile' not in self.__dict__:
        if not hasattr(self,'_profile'):
            self._profile,created = Profile.objects.get_or_create(id=self.id)
        return self._profile

    @property
    def vip(self):
        '''检查用户权限'''
        if not hasattr(self,'_vip'):
            self._vip = Vip.objects.get(id__in=self.vip_id)
        return self._vip




    def to_dict(self):
        return {
            'id':self.id,
            'nickname':self.nickname,
            'phonenum':self.phonenum,
            'sex':self.sex,
            'avatar':self.avatar,
            'location':self.location,
            'age':self.age
        }


    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class Profile(models.Model,ModelMixin):
    '''用户配置项'''
    location = models.CharField(max_length=32,verbose_name='目标城市')
    min_distance = models.IntegerField(default=1,verbose_name='最小距离')
    max_distance = models.IntegerField(default=10,verbose_name='最大距离')

    min_dating_age = models.IntegerField(default=18,verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=45,verbose_name='最大交友年龄')

    dating_sex = models.CharField(default='女',max_length=8,choices=(('男','男'),('女','女')),verbose_name='匹配性别')
    vibration = models.BooleanField(default=True,verbose_name='开启震动')
    only_matche = models.BooleanField(default=True,verbose_name='禁止其他人看相册')
    auto_play = models.BooleanField(default=True,verbose_name='是否自动播放视频')



    class Meta:
        db_table = 'profile'
        verbose_name = '用户配置信息'
        verbose_name_plural = verbose_name


