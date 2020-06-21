#!/bin/bash

LOCAL_DIR="./"  # 本地项目文件夹
REMOTE_DIR="/opt/swiper"

#登录服务器的配置
USER="xxxxx"
HOST="xxx.xxx.xxx.xxx"

rsync -crvP --exclude={.venv,.git,.vscode,logs,__pycache__} --delete $LOCAL_DIR/ $USER@$HOST:$REMOTE_DIR/

echo -e '文件同步完成\n'

# 在本地重启远程服务器
ssh $USER@$HOST "$REMOTE_DIR/scripts/restart.sh"
