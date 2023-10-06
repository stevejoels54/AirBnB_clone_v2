#!/usr/bin/env bash
# Sets up web servers for deployment of web_static

apt-get -y update
apt-get -y install nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

echo "joelofelectronics" > /data/web_static/releases/test/index.html

rm -f /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

location_alias="location /hbnb_static/ { alias /data/web_static/current/; }"
sed -i "/server_name _;/a $location_alias" /etc/nginx/sites-available/default

service nginx restart
