# _*_ coding:utf-8 _*_

from multiprocessing import cpu_count

bind = ['127.0.0.1:9000'] #线上环境不会开启在公网IP下,一般使用内网IP
daemon = True #是否开启守护进程模式
pidfile = 'logs/gunicorn.pid'

workers = cpu_count()*2
worker_class = 'gevent' #指定一个异步处理的库,gevent协程库
worker_connections = 65535

keepalive = 60  #服务器保持连接的时间,能够避免频繁的三次握手过程
timeout = 30
graceful_timeout = 10
forwarded_allow_ips = '*' #允许连接的IP


#日志处理
capture_output = True
loglevel = 'info'
errorlog = 'logs/error.log'