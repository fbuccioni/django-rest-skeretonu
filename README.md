django-skeretonu
=================


A skeleton for django framework.


Why all those dirs at the root?
-------------------------------

The reason I chose to use the `settings` and `wsgi` directories outside
the app, is because I need to standarize projects with multiple apps
to make containers or different orchrestration and automation scripts 
without the dependency of _"a main application"_ to start the applications.

Because those dirs are in the root folder, I decided to use an `/apps` 
folder in the root to put all apps there and make the skeleton tidy.

Additionally I use the folder `/automation` for `requierements.txt` and 
some other automation stuff like ssh keys, `fabfile.py` scripts, other
scripts, etc.

What is the `httpserver.py` file?
-----------------------------

The `httpserver.py` is a python script to run a 
[Tornado](http://www.tornadoweb.org) web server serving our Django project.

_**Note**_: If your project use static files, this script use static from 
`/static` folder, so you must run the  `collectstatic` django command 
before run this command.

_**Note**_: You must install the tornado python package before use this
script, this can be done via `pip` using the following command:

```
pip install tornado
```


### Usage:

```
python httpserver.py 9000
```

And the web server will be running in the port `9000`, the default host is
`0.0.0.0` binding the service to all ips. you can specify a host with `127.0.0.1:9000` argument.


Suggestions?
------------

All suggestions are always welcome, pleas feel free to ask in the issues
section of this repo.