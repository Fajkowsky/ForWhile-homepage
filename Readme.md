Heroku Django BasicApp
=====
This is simplest django webapplication with working out of box for heroku service. 

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


### Heroku

If you want run this on heroku you must have account there.

1. Login to heroku

        $ heroku login

2. Create app:

        $ heroku create

3. Push to heroku server:

        $ git push heroku master

3. Open in browser:

        $ heroku open

