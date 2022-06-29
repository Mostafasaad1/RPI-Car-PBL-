#!/bin/bash

python3 manage.py runserver 169.254.120.58:8000  & ./stream/mjpg_streamer -i "stream/input_uvc.so -d /dev/video0 -r 640x480 -f 60" -o "stream/output_http.so -w stream/www" 
