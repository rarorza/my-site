#!/bin/sh

set -e

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000

# docker-compose run --rm djangoapp apk add gettext
# python manage.py makemessages -l "pt_BR" -i 'venv'
# python manage.py compilemessages -l "pt_BR" -i 'venv
# python manage.py makemessages -l "en" -i 'venv'
# python manage.py compilemessages -l "en" -i 'venv'