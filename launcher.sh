apt update
apt install build-essential -y
apt install linux-headers-$(uname -r) -y
apt install make -y
apt install unzip -y
wget https://github.com/tlbem/nib_standard/archive/refs/heads/main.zip
unzip main.zip
chmod -R 7777 nib_standard-main
chmod -R 7777 nib_standard-main
cd nib_standard
make venv.python
