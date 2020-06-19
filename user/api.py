import os
from django.core import cache
from django.conf import settings

# Create your views here.
from common import error
from lib.http import render_json
from user.forms import ProfileForm
from user.logic import send_sms, check_vcode, save_upload_file
from user.models import User

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
    return render_json(None,0)

def login(request):
    '''短信验证登录'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if check_vcode(phonenum,vcode):
        #获取用户
        user,created= User.objects.get_or_create(phonenum=phonenum)

        #记录用户状态
        request.session['uid'] = user.id
        return render_json(user.to_dict(),0)
    else:
        return render_json(None,error.VCODE_ERROR)

def get_profile(request):
    '''获取个人资料'''
    user = request.user
    key = 'Profile-%s'%user.id
    user_profile = cache.get(key)
    if not user_profile:
        user_profile = user.profile.to_dict()
        cache.set(key,user_profile)
    return render_json(user_profile)

def modify_profile(request):
    '''修改个人资料'''
    form = ProfileForm(request.POST)
    if form.is_valid():
        user = request.user
        user.profile.__dict__.update(form.cleaned_data)
        user.profile.save()
        #修改缓存
        key = 'Profile-%s' % user.id
        cache.set(key, user.profile.to_dict())

        return render_json(None)
    else:
        return render_json(form.errors,error.PROFILE_ERROR)

def upload_avatar(request):
    '''头像上传'''
    #1,接受用户上传的头像
    #2.异步将头像上传到七牛云
    #3.将用户的头像的URL保存到数据库
    file = request.FILES.get('avatar')
    if file:
        save_upload_file(file,request)
        return render_json(None)
    else:
        return render_json(None,error.FILE_NOT_FOUND)
