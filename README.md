GeoDjango-Core
=======

GeoDjango is a sample app to test PostGIS

## Getting started

* Install requirements in the virtualenv

```
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

* Postgres setup

```
create user geodjango_admin with password 'your_db_passwd';
create database geodjango_core_db;
grant all privileges on database geodjango_core_db to geodjango_admin;
```

* Run the inital migrations

```
python manage.py migrate
```

* Change database and list all tables to verify

```
\c geodjango_core_db
\d+
```

* Run the server

```
python manage.py runserver
```

* When new migrations need to be created

```
python manage.py makemigrations
python manage.py migrate
```
### Development

If you wish to add additional options to settings file and not push those changes, set an environment variable `DJANGO_SETTINGS_MODULE` to `geodjango.local_settings`. This way, everytime you run `runserver`, it uses [local_settings.py](GeoDjango/local_settings.py)

### Testing
* To Use a different user for testing

```
create user test_geodjango with password 'password';
ALTER USER test_geodjango CREATEDB;
```

# Setting up using Docker

* Install Docker and Docker Compose from [here](https://docs.docker.com/compose/install/)
* Run ``` $ docker-compose build ```
* Initial Database setup
    - Run ```$ docker-compose up dbcreator```
    - Test that `geodjango_admin` role was created with ```$ docker-compose run dbcli``` and in the psql command prompt run ```=> \du```
* Now run migrations with the command ```$ docker-compose run web python manage.py migrate```
* Optionally create a superuser with  ```$ docker-compose run web python manage.py createsuperuser ```
* Once migrations are complete, you can run the server with the command ```$ docker-compose up web```. Then go to [localhost:8000](http://localhost:8000)

### Usage during development
* Develop as usual. The files remain in your host, but the apps and DBs run in containers
* Run the main app with the command ```$ docker-compose up -d web```. It starts the dependent containers and the main app and pushes it to the background
* To check the running containers, run ```$ docker-compose ps```
* To start/stop/restart any of the services/containers, run ```$ docker-compose start/stop/restart <name>```
* To check the logs of any service, run ```$ docker-compose logs <name>```
* To run general scripts/to log on to the containers, run ```$ docker-compose run <service> <command>```


# Getting staging arch set up in local
* Install docker-machine from [here](https://docs.docker.com/machine/)
* Create a local VBox machine by running ```$ docker-machine create --driver virtualbox dev```
* Change directory to beta
* Follow the aforementioned docker environment setup (dbcreator, migrations yada yada...)
