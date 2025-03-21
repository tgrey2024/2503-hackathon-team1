release: python manage.py makemigrations && python manage.py migrate && cd theme/static_src && npm install && npm run build && cd ../..
web: gunicorn project_root.wsgi:application
