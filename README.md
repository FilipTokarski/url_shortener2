[![Coverage Status](https://coveralls.io/repos/github/FilipTokarski/url_shortener2/badge.svg?branch=master)](https://coveralls.io/github/FilipTokarski/url_shortener2?branch=master)

## url_shortener2

This is a simple app for shortening urls. It gets url from user and returns shortened version, redy to use.

---

### Installation:

You can find full list of dependencies in 'requirements.txt'.

To run this app on your local machine, first make sure you have Python (version=3.7.2) installed. Go to your local folder and clone the repository:

```
$ cd [my_folder]
$ git clone [repository]
```

Create virtual Python environment and activate it:

```
$ python3 -m venv env
$ source env/bin/activate
```

Go to project folder and install all packages:

```
$ cd url_shortener2
$ pip install -r requirements.txt
```

Cd to app folder, make migrations and run server:

```
$ cd url_shortener
$ python manage.py makemigrations shortener
$ python manage.py migrate
$ python manage.py runserver
```

And you are ready to go!  
To get access to admin area, you need to create a super user:

```
$ python manage.py createsuperuser
```
