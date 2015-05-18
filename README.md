# martyrs
Hello I'm Islam Diaa
and this is a small Django app for tracking the martyrs of the 25th of January revolution.<br/>
works on Python 2.7.6 and Django 1.8
...

1-On your workspace create new folder martyrs and in this folder then create a new env<br/>
$ virtualenv env
<br/>
2-Then activate it :
<br/>
$ source env/bin/activate
<br/>
3- Install requirements :
<br/>
install django 1.8 latest version
<br/>
$ pip install Django==1.8
<br/>
and install mysql
$ pip install pymysql
<br/>
$ pip install MySQL-python
<br/>
" or "
just run
<br/>
$ pip install -r requirements.txt    # (to install all requirements)
<br/>

4- Clone latest version
<br/>
$ git clone https://github.com/esl4m/martyrs.git
<br/>

5- Create mysql Database :
<br/>
from terminal login to mysql 
$ mysql --user=root --password=root
<br/>
then create your database 
<br/>
$ create database martyrs ;
<br/>

6- Run Django Admin :<br/>
$ python manage.py runserver 
<br/>
then type on your browser 
<br/>
$ 127.0.0.1:8000/admin/
<br/>
username : admin & password : admin
<br/>
or create another super user : <br/>
$ python manage.py createsuperuser

7- Enjoy
