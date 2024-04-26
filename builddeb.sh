su - vagrant << EOF
cd /vagrant
python3 -m venv .builddebvenv
. .builddebvenv/bin/activate
pip install toml
pip install pyclean
PYTHONUNBUFFERED=true PYTHONPYCACHEPREFIX=/tmp/pycachep2 python3.11 builddeb.py build -p template
rm -rf .builddebvenv
EOF
