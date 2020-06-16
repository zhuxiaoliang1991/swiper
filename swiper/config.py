
from http.client import HTTPConnection
from urllib.parse import urlencode



host  = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

#用户名是登录用户中心->验证码短信->产品总览->APIID
account  = "C23191331" 
#密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
password = "6d845cf20bea6010c1de3198d20b0b7e"
text = "您的验证码是：%s。请不要把验证码泄露给其他人。"
params = {'account': account, 'password' : password, 'content': text, 'mobile':None,'format':'json' }
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}







