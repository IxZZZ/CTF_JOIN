#!/bin/bash

mkdir -p simpleweb/log simpleweb/session simpleweb/uploads
chown -R 0:1000 simpleweb/
chmod -R 744 simpleweb/users
chmod -R 744 simpleweb/flag_*
chmod -R 777 simpleweb/log simpleweb/session simpleweb/uploads
chmod -R 755 simpleweb/web simpleweb/www
chmod 755 simpleweb/webcgi.cgi
docker-compose up -d