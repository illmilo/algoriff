#!/bin/bash
echo "BUILD START"
python3 -m pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput

mkdir -p staticfiles_build/media/
cp -r media/* staticfiles_build/media/

echo "BUILD END"