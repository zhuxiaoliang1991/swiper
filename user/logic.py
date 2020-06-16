import json
import random
import string
from http.client import HTTPConnection
from urllib.parse import urlencode
from django.core.cache import cache
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
    response_str = json.dumps(response.read())
    conn.close()
    return response_str