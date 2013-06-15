============
Lifespan App
============
Anton: inside there are my experiments with lifespan and chats.

Warning: temporaly you will have to do:

cake build

on semantic folder inside static


Setup
=====

1. Git in::

   git clone https://github.com/denigma/lifespan

       vitualenv env

       . env/bin/activate

       pip install -r requirements.txt

       ./manage.py syncdb
       ./manage.py runserver

2. Install Nodejs, CoffeeScript and LESS::

    Install nodejs ( http://nodejs.org/ ).
    Nodejs is used as a compiler for CoffeeScript and LESS
    It is better to install the version from the website as various linux repositories contain outdated versions

    After installation you will have npm at your disposal.
    With npm install:
    sudo npm install -g coffeescript
    sudo npm install -g batman
    sudo npm install -g less

