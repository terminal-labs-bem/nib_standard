apt update
apt install build-essential -y
apt install linux-headers-$(uname -r) -y
apt install make -y
apt install unzip -y
wget https://github.com/terminal-labs/standard_nib/archive/refs/heads/main.zip
unzip main.zip
chmod -R 7777 standard_nib-main
cd standard_nib-main
make psf
