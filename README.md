ForWhile basic page
=====
Simple maina page for forwhile.
!(Base)[https://raw.githubusercontent.com/Fajkowsky/ForWhile-homepage/master/static/img/screenshot_1.png]

Deployment
----------

All what you need to do after fork this repository is:
### Local
If you want run this on local machine you should have installed heroku-toolbelt and virtualenv.

1. Create virtual environment:

        $ virtualenv venv/ --distribute

2. Activate virtual environment:

        $ source venv/bin/activate

3. Install requirements:

        $ pip install -r requirements.txt


4. Run app:

        $ python manage.py runserver 
 or

        $ foreman start