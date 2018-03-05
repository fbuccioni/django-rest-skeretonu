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


Suggestions?
------------

All suggestions are always welcome, pleas feel free to ask in the issues
section of this repo.