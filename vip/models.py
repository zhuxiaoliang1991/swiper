from django.db import models

# Create your models here.
class Vip(models.Model):
    name = models.CharField(max_length=32,unique=True)
    level = models.IntegerField()
    price = models.FloatField()

    def had_perm(self,perm_name):
        '''检查是否有某种权限'''
        perm = Permission.objects.get(name=perm_name)
        return VipPremRelation.objects.filter(vip_id=self.id,perm_id=perm.id).exists()

    def perms(self):
       '''当前vip具有的所有的权限'''
        relations = VipPremRelation.objects.filter(vip_id=self.id)
        perm_id_list = [r.perm_id for r in relations]
        return Permission.objects.filter(id__in=perm_id_list)




class Permission(models.Model):
    '''
    会员身份标识
    超级喜欢
    反悔功能
    任意更改定位
    无限喜欢次数
    '''

    name = models.CharField(max_length=32,unique=True)


class VipPremRelation(models.Model):
    '''会员-权限关系表'''
    vip_id = models.IntegerField()
    perm_id = models.IntegerField()