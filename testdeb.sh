cd /vagrant
python3 -m venv /dev/shm/.testdebvenv
. /dev/shm/.testdebvenv/bin/activate
sudo PYTHONUNBUFFERED=true PYTHONPYCACHEPREFIX=/tmp/pycachep2 python3.11 testdeb.py test -p template
rm -rf /dev/shm/.testdebvenv
