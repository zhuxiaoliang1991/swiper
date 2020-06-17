

from django.core import cache


# Create your views here.
from common import error
from lib.http import render_json
from user.logic import send_sms,check_vcode
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
    return render_json(user.profile.to_dict(),0)

def modify_profile(request):
    '''修改个人资料'''
    pass

def upload_avatar(request):
    '''头像上传'''
    pass