from django.shortcuts import render
from social import logic
import logging

# Create your views here.
from lib.http import render_json
from social.models import Friend
from vip.logic import perm_require

log = logging.getLogger('inf')

def get_users(request):
    '''获取推荐列表'''
    group_num = int(request.GET.get('group_num',0))
    start = group_num * 5
    end = start + 5
    users = logic.get_rcmd_user(request.user)[start:end]
    result = [user.to_dict() for user in users]
    return render_json(result)


def like(request):
    '''喜欢'''
    sid = int(request.POST.get('sid'))
    is_match = logic.like(request.user,sid)
    log.info(f'{request.user.id} like {sid}')
    return render_json({'is_match':is_match})

@perm_require('superlike')
def superlike(request):
    '''超级喜欢'''
    sid = int(request.POST.get('sid'))
    is_match = logic.superlike(request.user, sid)
    log.info(f'{request.user.id} superlike {sid}')
    return render_json({'is_match': is_match})
def dislike(request):
    '''不喜欢'''
    sid = int(request.POST.get('sid'))
    logic.dislike(request.user,sid)
    log.info(f'{request.user.id} dislike {sid}')
    return render_json(None)

@perm_require('rewind')
def rewind(request):
    '''反悔'''
    sid = int(request.POST.get('sid'))
    logic.rewind(request.user, sid)
    return render_json(None)

def friends(request):
    '''好友列表'''
    my_friends = Friend.friends(request.user.id)
    friends_info = [frd.to_dict() for frd in my_friends]
    return render_json({'friends':friends_info})