#!/usr/bin/env bash
# starts up flask app

export APP_SECRET=`openssl rand -base64 32`

exec gunicorn -w 3 -b 0.0.0.0:5000 --access-logfile - --error-logfile - login:app
