import json
import random
import string
from http.client import HTTPConnection
from urllib.parse import urlencode, urljoin

import os
from django.conf import settings
from django.core.cache import cache

from lib.qncloud import async_upload_to_qiniu
from worker import call_by_worker

from swiper import config



def gen_verify_code(length=6):
    verify_code_list = random.choices(string.digits,k=length)
    return ''.join(verify_code_list)

@call_by_worker
def send_sms(phonenum):
    vcode = gen_verify_code()
    #将验证码存入缓存
    key = 'VerifyCode-%s'%phonenum
    cache.set(key,vcode,120)

    sms_cfg = config.params.copy()
    sms_cfg['content'] = sms_cfg['content']%vcode
    sms_cfg['mobile'] = phonenum
    params = urlencode(sms_cfg)
    conn = HTTPConnection(config.host, port=80, timeout=30)
    conn.request("POST", config.sms_send_uri, params, config.headers)
    response = conn.getresponse()
    response_str = json.loads(response.read())
    conn.close()
    return response_str


def check_vcode(phonenum,vcode):
    '''检查验证码是否正确'''
    key = 'VerifyCode-%s'%phonenum
    saved_vcode = cache.get(key)
    return saved_vcode == vcode

def save_upload_file(upload_file,request):
    '''保存上传文件,并上传到七牛云'''
    #获取文件并保存到本地
    ext_name = upload_file.name.split('.')[-1]
    filename = 'Avatar-%s.%s' % (request.session['uid'], ext_name)
    filepath = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)
    with open(filepath, 'wb') as newfile:
        for chunk in upload_file.chunks():
            newfile.write(chunk)
    #异步将头像上传到七牛云
    async_upload_to_qiniu(filepath,filename)
    #保存url到数据库
    url = urljoin(config.QN_BASE_URL,filename)
    user = request.user
    user.avatar = url
    user.save()