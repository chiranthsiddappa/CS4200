apt-get update -y
apt-get install -y git help2man perl python3 python3-pip python3-venv make autoconf g++ flex bison ccache
apt-get install -y libgoogle-perftools-dev numactl perl-doc
apt-get install -y libfl2 libfl-dev mold
apt-get install -y perl-doc
git clone https://github.com/verilator/verilator.git
pushd verilator
git checkout v5.026
autoconf
./configure
make -j 2
make install
popd
