sudo apt-get update
sudo apt-get install -y mongodb python2.7 python-pip python-virtualenv build-essential python-dev
sudo restart mongodb
virtualenv flaskpaste --distribute
# curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py | python
source ~/flaskpaste/bin/activate
sudo pip install -r /vagrant/pip_requirements.txt
python /vagrant/flaskpaste.py