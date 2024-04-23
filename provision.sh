DEBIAN_FRONTEND=noninteractive
echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
apt-get install -y -q

apt-get update -y
apt-get upgrade -y

apt-get install incus/bookworm-backports -y
chmod 777 /var/lib/incus/unix.socket
incus admin init --minimal

apt-get install build-essential dkms gdb -y
apt-get install lsb-release software-properties-common gnupg -y
apt-get install debhelper dh-python dh-virtualenv -y
apt-get install libpcre3 libpcre3-dev -y
apt-get install uuid uuid-dev -y
apt-get install lzma lzma-dev -y
apt-get install liblzma-dev zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev -y
apt-get install curl -y
apt-get install wget -y

apt-get install tree bc -y

apt-get install git -y

apt-get install python3-pip -y
apt-get install python3.11 -y
apt-get install python3.11-dev -y
apt-get install python3.11-venv -y

apt-get install python-is-python3 -y
ln -s /usr/bin/python3.11 /usr/bin/python3.11.2

apt-get install glances -y

pip3 install shell-functools --break-system-packages

apt-get install lighttpd -y
sudo ln -s /usr/sbin/lighttpd /usr/local/bin/lighttpd

apt-get install busybox -y

wget https://apt.llvm.org/llvm.sh
chmod u+x llvm.sh
./llvm.sh 17

apt-get install clang-17 lldb-17 lld-17 -y
apt-get install libllvm-17-ocaml-dev libllvm17 llvm-17 llvm-17-dev llvm-17-doc llvm-17-examples llvm-17-runtime -y
apt-get install clang-17 clang-tools-17 clang-17-doc libclang-common-17-dev libclang-17-dev libclang1-17 clang-format-17 python3-clang-17 clangd-17 clang-tidy-17 -y
apt-get install clang-17 lldb-17 lld-17 clangd-17 clang-tidy-17 clang-format-17 clang-tools-17 llvm-17-dev lld-17 lldb-17 llvm-17-tools libomp-17-dev libc++-17-dev libc++abi-17-dev libclang-common-17-dev libclang-17-dev libclang-cpp17-dev libunwind-17-dev libclang-rt-17-dev libpolly-17-dev -y
apt-get install libc++-17-dev libc++abi-17-dev -y
apt-get install flang-17 -y

ln -s /usr/bin/clang-17 /usr/bin/clang
ln -s /usr/bin/clang++-17 /usr/bin/clang++
update-alternatives --install /usr/bin/cc cc /usr/bin/clang 100
update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++ 100

rm llvm.sh

RUSTUP_HOME=/opt/rust
export RUSTUP_HOME
CARGO_HOME=/opt/rust
export CARGO_HOME
curl https://sh.rustup.rs -sSf | sh -s -- -y --no-modify-path &> /dev/null

cat > /usr/local/bin/cargo <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rust exec /opt/rust/bin/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/cargo

cat > /usr/local/bin/cargo-clippy <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rust exec /opt/rust/bin/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/cargo-clippy

cat > /usr/local/bin/cargo-fmt <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rust exec /opt/rust/bin/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/cargo-fmt

cat > /usr/local/bin/cargo-miri <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rust exec /opt/rust/bin/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/cargo-miri

cat > /usr/local/bin/clippy-driver <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rust exec /opt/rust/bin/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/clippy-driver

cat > /usr/local/bin/rls <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rust exec /opt/rust/bin/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/rls

cat > /usr/local/bin/rust-analyzer <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rust exec /opt/rust/bin/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/rust-analyzer

cat > /usr/local/bin/rust-gdb <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rust exec /opt/rust/bin/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/rust-gdb

cat > /usr/local/bin/rust-gdbgui <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rust exec /opt/rust/bin/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/rust-gdbgui

cat > /usr/local/bin/rust-lldb <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rust exec /opt/rust/bin/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/rust-lldb

cat > /usr/local/bin/rustc <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rust exec /opt/rust/bin/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/rustc

cat > /usr/local/bin/rustdoc <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rust exec /opt/rust/bin/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/rustdoc

cat > /usr/local/bin/rustfmt <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rust exec /opt/rust/bin/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/rustfmt

cat > /usr/local/bin/rustup <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rust exec /opt/rust/bin/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/rustup

pip3 install rustenv --break-system-packages

curl -sSf https://rye-up.com/get | RYE_HOME=/opt/rye RYE_VERSION="0.32.0" RYE_TOOLCHAIN_VERSION="3.11.8" RYE_INSTALL_OPTION="--yes" bash &> /dev/null
cat > /usr/local/bin/rye <<EOF
#!/bin/sh
RUSTUP_HOME=/opt/rye exec /opt/rye/shims/\${0##*/} "\$@"
EOF
chmod +x /usr/local/bin/rye
rye config --set-bool behavior.global-python=false

su - vagrant << EOF
curl -sSf https://rye-up.com/get | RYE_VERSION="0.32.0" RYE_TOOLCHAIN_VERSION="3.11.8" RYE_INSTALL_OPTION="--yes" bash &> /dev/null
rye config --set-bool behavior.global-python=false
EOF

cargo install minijinja-cli --root /
cargo install du-dust --root /
cargo install procs --root /
cargo install just --root /
cargo install bat --root /
cargo install sd --root /

python --version
python3 --version
python3.11 --version
python3.11.2 --version
cargo --version
rustc --version
rye --version
