web: gunicorn hotel-website.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn hotel-website.wsgi