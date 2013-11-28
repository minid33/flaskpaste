flaskpaste
==========

A simple python pastebin based on Flask, MongoDB and PrismJS


Yet another pastebin
--------------------

I created this pastebin to show that CRUD in mongodb is simple, that pastebins are a simple problem to solve and should not be complicated to deploy.

Requirements
------------
This package was made for python 2.7.X
We run it on windows, we've also run it on Ubuntu.
A MongoDB Server v2.2.1 or above

Installing the Pastebin
-----------------------
1. Install the pip requirements on your virtualenv or interpreter `pip install -r pip_requirements.txt`
2. Rename example_app.cfg to app.cfg
3. Change the settings in app.cfg to match your environment
4. `python flaskpaste.py`

If you're going for a fresh install on Linux bootstrap.sh may end up doing all this for you (No promises).
