# martyrs
Hello I'm Islam Diaa
and this is a small Django app for tracking the martyrs of the 25th of January revolution.<br/>
works on Python 2.7.6 and Django 1.8
<br/>
* On your workspace create new folder martyrs and in this folder then create a new env<br/>
```
$ virtualenv env
```
* Then activate it :
```
$ source env/bin/activate
```
* Install requirements :
install django 1.8 latest version
```
$ pip install Django==1.8
```
and install mysql
```
$ pip install pymysql
$ pip install MySQL-python
```
" or " just run
```
$ pip install -r requirements.txt    # (to install all requirements)
```

* Clone latest version
```
$ git clone https://github.com/esl4m/martyrs.git
```

* Create mysql Database :
<br/>
from terminal login to mysql 
```
$ mysql --user=root --password=root
```
then create your database 
```
$ create database martyrs ;
```
* Run Django Admin :
```
$ python manage.py runserver 
```
then type on your browser 
```
$ 127.0.0.1:8000/admin/
```
username : admin & password : admin
<br/>
or create another super user :
```
$ python manage.py createsuperuser
```
* Enjoy
