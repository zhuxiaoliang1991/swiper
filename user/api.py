from django.core import cache
from django.shortcuts import render

# Create your views here.
from user.logic import send_sms

'''
需要实现的内容:
    - 手机注册
    - 短信验证登录
    - 获取个人资料
    - 头像上传
'''

def get_verify_code(request):
    '''手机注册'''
    phonenum = request.GET.get('phonenum')
    send_sms(phonenum)

def login(request):
    '''短信验证登录'''
    vcode = cache.get()
    pass

def get_profile(request):
    '''获取个人资料'''
    pass

def modify_profile(request):
    '''修改个人资料'''
    pass

def upload_avatar(request):
    '''头像上传'''
    pass