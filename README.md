
# DJANGO LAB PROGRAMS VTU

The repo contains all the programs of Django(Fullstack Development) for VTU 6th semester (21CS62).


Below are the steps for running the programs Locally




## Requirements
Python

MySQL client

## Installation

Install django

```bash
  pip install django
```
* Install the MySQL client (mysqlclient).
* Create a MySQL database using the MySQL command-line tool or a GUI tool.
* Configure the DATABASES setting in settings.py

```bash
  pip install mysqlclient
```

```bash
  cd ..
```

Create and Activate a Virtual Environment
```bash
  python -m venv venv
 .\venv\Scripts\activate
```
```bash
  cd django-project
```

Install Dependencies

```bash
  python install -r requirements.txt
```
Set Up the Database
```bash
  python manage.py migrate
```
Create super user(optional)

```bash
  python manage.py createsuperuser
```
Run server
```bash
  python manage.py runserver
```

##open the localhost link after running the server and use the URLs accordingly
```
http://localhost:8080/mod4-2/
```
