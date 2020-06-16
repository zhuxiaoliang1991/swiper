from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=32,unique=True,verbose_name='昵称')
    phonenum = models.CharField(max_length=16,unique=True,verbose_name='手机号')
    sex = models.CharField(max_length=8,choices=(('男','男'),('男','女')),verbose_name='性别')
    birth_year = models.IntegerField(verbose_name='出生年份')
    birth_month = models.IntegerField(verbose_name='出生月份')
    birth_day = models.IntegerField(verbose_name='出生日期')
    avatar = models.CharField(max_length=256,verbose_name='头像url')
    location = models.CharField(max_length=32,verbose_name='常居地址')

    @property
    def age(self):
        now = datetime.date.today()
        birth_date = datetime.date(
            self.birth_year,self.birth_month,self.birth_day
        )
        #返回年龄
        return (now - birth_date).days//365




