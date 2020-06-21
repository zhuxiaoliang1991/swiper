#!/bin/bash

#远程项目目录
PROJECT_DIR="/opt/swiper"

cd $PROJECT_DIR
source .venv/bin/activate
gunicorn -c $PROJECT_DIR/swiper/gconfig.py swiper.wsgi
deactivate
cd -
