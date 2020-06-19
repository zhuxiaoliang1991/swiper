from django.http import response
from django.shortcuts import render
from lib.http import render_json
from common import error
# Create your views here.
import logging

log = logging.getLogger('err')
def perm_require(need_perm):
    #权限检查装饰器
    def deco(view_func):
        def wrap(request):
            user = request.user
            if user.vip.had_perm(need_perm):
                view_func(request)
                return response
            else:
                log.error(f'{request.user.nickname} not has {need_perm}')
                return render_json(None,error.NOT_HAS_PERM)
        return wrap
    return deco