#!/bin/bash

PROJECT_DIR="/opt/swiper"

#关掉gunicorn
PID=`cat $PROJECT_DIR/logs/gunicorn.pid`

kill $PID


#或者 cat $PROJECT_DIR/logs/gunicorn.pid | xargs kill